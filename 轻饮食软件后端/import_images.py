"""
从 HowToCook 仓库下载食谱图片到轻食刻
使用 GitHub API + media.githubusercontent.com 获取 LFS 图片
"""
import os
import re
import json
import urllib.request
import urllib.parse
from app import create_app
from models import db
from models.food import Food

GITHUB_REPO = 'Anduin2017/HowToCook'
GITHUB_BRANCH = 'master'
MEDIA_BASE = f'https://media.githubusercontent.com/media/{GITHUB_REPO}/{GITHUB_BRANCH}'
API_BASE = f'https://api.github.com/repos/{GITHUB_REPO}/git/trees/{GITHUB_BRANCH}'
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads', 'recipes')

# 优先选择的图片关键词（成品 > 完成 > 出锅 > 装盘 > 摆盘）
PRIORITY_KEYWORDS = ['成品', '完成', '出锅', '装盘', '摆盘']


def get_image_tree():
    """从 GitHub API 获取所有图片文件路径"""
    url = f'{API_BASE}?recursive=1'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/vnd.github.v3+json'
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    # 按菜品名分组图片
    dish_images = {}
    for item in data.get('tree', []):
        path = item['path']
        if not path.startswith('dishes/') or not path.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            continue
        # 解析: dishes/{category}/{dish_name}/{image_file}
        parts = path.split('/')
        if len(parts) >= 4:
            dish_name = parts[2]
            if dish_name not in dish_images:
                dish_images[dish_name] = []
            dish_images[dish_name].append(path)

    return dish_images


def find_best_image(image_paths, dish_name=''):
    """从多张图片中选择最佳的一张（优先成品图）"""
    if not image_paths:
        return None

    # 按优先级排序
    for keyword in PRIORITY_KEYWORDS:
        for path in image_paths:
            filename = os.path.basename(path)
            if keyword in filename:
                return path

    # 包含菜品名的优先
    if dish_name:
        for path in image_paths:
            filename = os.path.basename(path)
            if dish_name in filename:
                return path

    # 默认返回第一张
    return image_paths[0]


def download_image(github_path):
    """从 GitHub 下载单张图片"""
    encoded_path = urllib.parse.quote(github_path)
    url = f'{MEDIA_BASE}/{encoded_path}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def import_images():
    """下载图片并更新数据库"""
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # 从 GitHub 获取图片列表
    print('正在从 GitHub 获取食谱图片列表...')
    dish_images = get_image_tree()
    print(f'找到 {len(dish_images)} 个食谱有图片')

    app = create_app()
    with app.app_context():
        updated = 0
        skipped = 0
        failed = 0
        not_found = 0

        for dish_name, image_paths in dish_images.items():
            # 在数据库中查找匹配的食谱
            food = Food.query.filter(Food.name.like(f'%{dish_name}%')).first()
            if not food:
                not_found += 1
                continue

            # 如果已有图片且文件存在，跳过
            if food.image:
                local_file = os.path.join(UPLOAD_DIR, os.path.basename(food.image))
                if os.path.exists(local_file) and os.path.getsize(local_file) > 1000:
                    skipped += 1
                    continue

            # 选择最佳图片
            best_path = find_best_image(image_paths, dish_name)
            if not best_path:
                continue

            # 下载图片
            try:
                image_data = download_image(best_path)
                if len(image_data) < 1000:
                    print(f'  跳过 {dish_name}: 图片太小 ({len(image_data)} bytes)')
                    failed += 1
                    continue

                # 保存到本地
                ext = os.path.splitext(best_path)[1]
                safe_name = re.sub(r'[^\w一-鿿]', '_', dish_name)
                dest_filename = f'{safe_name}{ext}'
                dest_path = os.path.join(UPLOAD_DIR, dest_filename)

                with open(dest_path, 'wb') as f:
                    f.write(image_data)

                # 更新数据库
                food.image = f'/api/uploads/recipes/{dest_filename}'
                updated += 1

                if updated % 20 == 0:
                    print(f'  已下载 {updated} 张图片...')

            except Exception as e:
                print(f'  下载失败 {dish_name}: {e}')
                failed += 1

        db.session.commit()
        print(f'\n导入完成:')
        print(f'  成功下载: {updated} 张')
        print(f'  已存在跳过: {skipped} 张')
        print(f'  下载失败: {failed} 张')
        print(f'  未匹配数据库: {not_found} 个')


if __name__ == '__main__':
    import_images()
