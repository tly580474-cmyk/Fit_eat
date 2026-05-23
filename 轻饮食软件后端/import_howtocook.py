"""
从 HowToCook 仓库导入食谱数据到轻食刻数据库
"""
import os
import re
import json
from app import create_app
from models import db
from models.food import Food

HOWTOCOOK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '..', '食谱数据借鉴', 'HowToCook', 'HowToCook-master', 'dishes')

# 分类映射：HowToCook 目录名 -> 轻食刻 meal_type
CATEGORY_MAP = {
    'breakfast': 'breakfast',
    'meat_dish': 'lunch',
    'vegetable_dish': 'lunch',
    'aquatic': 'dinner',
    'staple': 'lunch',
    'soup': 'dinner',
    'dessert': 'snack',
    'drink': 'snack',
    'condiment': 'lunch',
    'semi-finished': 'lunch',
}

# 分类标签
CATEGORY_TAGS = {
    'breakfast': '早餐',
    'meat_dish': '荤菜,家常菜',
    'vegetable_dish': '素菜,家常菜',
    'aquatic': '水产,海鲜',
    'staple': '主食',
    'soup': '汤羹,暖胃',
    'dessert': '甜品,下午茶',
    'drink': '饮品',
    'condiment': '酱料',
    'semi-finished': '半成品',
}


def parse_ingredient(text):
    """解析食材字符串为 {name, amount} 格式"""
    text = text.strip()
    if not text:
        return None

    # 清除 Markdown 语法
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # 链接
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # 加粗
    text = re.sub(r'\*([^*]+)\*', r'\1', text)  # 斜体

    # 尝试匹配常见的食材格式
    # 格式1: "食材名 数量单位" 如 "巴沙鱼 500g"
    # 格式2: "食材名，数量单位" 如 "黑鳕鱼，带皮，2 片，450g"
    # 格式3: "食材名 = 数量" 如 "八角 = 一个"

    # 先尝试用 = 分割
    if '=' in text:
        parts = text.split('=', 1)
        name = parts[0].strip()
        amount = parts[1].strip()
        return {'name': name, 'amount': amount}

    # 尝试匹配 "食材名 数量+单位" 的模式
    # 匹配数字开头或数字+单位的模式
    units = 'g|ml|kg|l|升|个|枚|片|块|根|条|只|颗|粒|瓣|朵|勺|汤匙|茶匙|碗|杯|把|束|份|包|袋|盒|瓶|罐|小块|适量|少许|若干'
    match = re.match(r'^(.+?)\s+(\d[\d\s./]*(?:' + units + ').*)$', text)
    if match:
        return {'name': match.group(1).strip(), 'amount': match.group(2).strip()}

    # 匹配 "食材名，描述，数量" 的模式
    match = re.match(r'^([^，,]+)[，,](.+)$', text)
    if match:
        name = match.group(1).strip()
        rest = match.group(2).strip()
        # 尝试从 rest 中提取数量
        amount_match = re.search(r'(\d[\d\s./]*(?:' + units + ')?)', rest)
        if amount_match:
            return {'name': name, 'amount': amount_match.group(1).strip()}
        return {'name': name, 'amount': rest}

    # 如果都没有匹配，返回整个文本作为名称，数量为空
    return {'name': text, 'amount': '适量'}


def clean_markdown(text):
    """清除文本中的 Markdown 语法"""
    if not text:
        return text
    # 清除图片语法 ![alt](url)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    # 清除链接语法 [text](url)，保留文字
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # 清除加粗 **text**
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # 清除斜体 *text*
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # 清除行内代码 `text`
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # 清除多余空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def parse_recipe(filepath, category):
    """解析单个食谱 markdown 文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取标题
    title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    if not title_match:
        return None
    title = title_match.group(1).strip()
    # 去掉 "的做法" 后缀
    title = re.sub(r'的做法$', '', title)

    # 提取描述（标题后的第一段非空文本）
    desc = ''
    after_title = content[title_match.end():].strip()
    desc_match = re.match(r'^(.+?)(?:\n\n|\n#)', after_title, re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # 去掉难度和卡路里行
        desc = re.sub(r'预估烹饪难度：[★]+\n?', '', desc)
        desc = re.sub(r'预估卡路里：.*?\n?', '', desc)
        # 去掉 Markdown 图片语法 ![alt](url)
        desc = re.sub(r'!\[.*?\]\(.*?\)', '', desc)
        desc = desc.strip()

    # 提取卡路里
    calories = 0
    cal_match = re.search(r'预估卡路里[：:]\s*(\d+)', content)
    if cal_match:
        calories = int(cal_match.group(1))

    # 提取难度
    difficulty = '简单'
    diff_match = re.search(r'预估烹饪难度[：:]\s*(★+)', content)
    if diff_match:
        stars = len(diff_match.group(1))
        if stars <= 2:
            difficulty = '简单'
        elif stars <= 3:
            difficulty = '中等'
        else:
            difficulty = '较难'

    # 提取计算/配料部分
    ingredients = []
    calc_match = re.search(r'##\s*计算\s*\n([\s\S]*?)(?=\n##|\Z)', content)
    if calc_match:
        calc_text = calc_match.group(1)
        for line in calc_text.split('\n'):
            line = line.strip()
            # 支持 - 和 * 两种列表标记
            if (line.startswith('-') or line.startswith('*')):
                item = re.sub(r'^[-*]\s*', '', line).strip()
                if item and '份数' not in item:
                    parsed = parse_ingredient(item)
                    if parsed:
                        ingredients.append(parsed)

    # 如果计算部分没找到配料，从必备原料部分提取
    if not ingredients:
        req_match = re.search(r'##\s*必备原料和工具\s*\n([\s\S]*?)(?=\n##|\Z)', content)
        if req_match:
            for line in req_match.group(1).split('\n'):
                line = line.strip()
                # 支持 - 和 * 两种列表标记
                if line.startswith('-') or line.startswith('*'):
                    item = re.sub(r'^[-*]\s*', '', line).strip()
                    if item:
                        parsed = parse_ingredient(item)
                        if parsed:
                            ingredients.append(parsed)

    # 提取操作步骤
    steps = []
    ops_match = re.search(r'##\s*操作\s*\n([\s\S]*?)(?=\n##|\Z)', content)
    if ops_match:
        for line in ops_match.group(1).split('\n'):
            line = line.strip()
            match = re.match(r'^\d+[\.\、]\s*(.+)', line)
            if match:
                step_desc = clean_markdown(match.group(1).strip())
                steps.append({'title': f'步骤{len(steps)+1}', 'desc': step_desc})

    # 提取附加内容/小贴士
    benefits = ''
    extra_match = re.search(r'##\s*附加内容\s*\n([\s\S]*?)(?=\n##|\Z)', content)
    if extra_match:
        tips = []
        for line in extra_match.group(1).split('\n'):
            line = line.strip()
            if line.startswith('-'):
                tip = clean_markdown(line.lstrip('- ').strip())
                if tip:
                    tips.append(tip)
        benefits = '；'.join(tips) if tips else ''

    # 如果没有描述，用标题生成
    if not desc:
        desc = f'一道美味的{title}'

    # 如果没有卡路里，根据分类估算
    if calories == 0:
        cal_estimates = {
            'breakfast': 350, 'meat_dish': 500, 'vegetable_dish': 200,
            'aquatic': 350, 'staple': 400, 'soup': 200,
            'dessert': 300, 'drink': 150, 'condiment': 100, 'semi-finished': 400,
        }
        calories = cal_estimates.get(category, 300)

    # 根据卡路里估算宏量营养素（粗略估算）
    protein = round(calories * 0.15 / 4, 1)  # 15% 来自蛋白质
    carbs = round(calories * 0.50 / 4, 1)    # 50% 来自碳水
    fat = round(calories * 0.35 / 9, 1)      # 35% 来自脂肪

    return {
        'name': title,
        'description': desc[:500],
        'calories': calories,
        'protein': protein,
        'carbs': carbs,
        'fat': fat,
        'fiber': 3.0,
        'tags': CATEGORY_TAGS.get(category, ''),
        'ingredients': json.dumps(ingredients, ensure_ascii=False),
        'steps': json.dumps(steps, ensure_ascii=False),
        'benefits': benefits[:500],
        'prep_time': '30分钟',
        'difficulty': difficulty,
        'meal_type': CATEGORY_MAP.get(category, 'lunch'),
    }


def import_recipes():
    """导入所有食谱"""
    if not os.path.exists(HOWTOCOOK_DIR):
        print(f'错误：找不到 HowToCook 目录: {HOWTOCOOK_DIR}')
        return

    recipes = []
    categories = os.listdir(HOWTOCOOK_DIR)

    for category in categories:
        cat_dir = os.path.join(HOWTOCOOK_DIR, category)
        if not os.path.isdir(cat_dir) or category == 'template':
            continue

        for item in os.listdir(cat_dir):
            item_path = os.path.join(cat_dir, item)
            if os.path.isfile(item_path) and item.endswith('.md'):
                recipe = parse_recipe(item_path, category)
                if recipe:
                    recipes.append(recipe)
            elif os.path.isdir(item_path):
                # 有些食谱是目录，里面可能有多个 md 文件
                for sub_item in os.listdir(item_path):
                    if sub_item.endswith('.md'):
                        recipe = parse_recipe(os.path.join(item_path, sub_item), category)
                        if recipe:
                            recipes.append(recipe)

    print(f'共解析到 {len(recipes)} 个食谱')

    # 写入数据库
    app = create_app()
    with app.app_context():
        # 先清除已存在的同名食谱（避免重复导入）
        existing_names = {r['name'] for r in recipes}
        existing = Food.query.filter(Food.name.in_(existing_names)).all()
        if existing:
            print(f'删除 {len(existing)} 条旧的 HowToCook 数据...')
            for f in existing:
                db.session.delete(f)
            db.session.commit()

        # 批量插入
        for r in recipes:
            food = Food(**r)
            db.session.add(food)

        db.session.commit()
        print(f'成功导入 {len(recipes)} 个食谱到数据库')


if __name__ == '__main__':
    import_recipes()
