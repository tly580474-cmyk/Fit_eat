import json
from app import create_app
from models import db
from models.user import User
from models.food import Food
from models.achievement import Achievement

app = create_app()


def init_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('数据库表已创建')

        # 创建管理员用户
        admin = User(
            username='admin',
            email='admin@lightdiet.com',
            gender='女',
            age=25,
            height=165,
            weight=58,
            body_fat=22,
            target_calories=1800,
            target_weight=55,
            plan_days=42,
            bio='越自律，越自由 | 坚持轻食第 42 天'
        )
        admin.set_password('admin123')
        db.session.add(admin)

        # 创建示例用户
        user1 = User(
            username='林小悦',
            email='lin@example.com',
            gender='女',
            age=24,
            height=163,
            weight=55,
            target_calories=1600,
            target_weight=52,
            plan_days=30
        )
        user1.set_password('123456')
        db.session.add(user1)

        # 创建食物数据
        foods = [
            Food(
                name='牛油果水波蛋活力碗',
                description='这款活力碗完美平衡了优质脂肪、蛋白质和复合碳水，是开启元气满满一天的理想选择。',
                calories=345, protein=18, carbs=24, fat=12, fiber=6,
                tags='高蛋白,低GI',
                ingredients=json.dumps([
                    {'name': '熟透牛油果', 'amount': '1/2个'},
                    {'name': '新鲜鸡蛋', 'amount': '1枚'},
                    {'name': '全麦欧包', 'amount': '1片'},
                    {'name': '樱桃番茄', 'amount': '5-6个'}
                ]),
                steps=json.dumps([
                    {'title': '准备牛油果泥', 'desc': '将牛油果切开去核，取出果肉压碎。加入少许柠檬汁、海盐和黑胡椒，搅拌至质地顺滑。'},
                    {'title': '制作水波蛋', 'desc': '锅中烧开水，加入一勺白醋。用勺子在水中搅出一个旋涡，缓缓倒入打好的鸡蛋，微火煮3分钟。'},
                    {'title': '组装装盘', 'desc': '在烤好的欧包上抹上牛油果泥，放上水波蛋，点缀切开的樱桃番茄，撒上奇亚籽即可。'}
                ]),
                benefits='牛油果富含单不饱和脂肪酸，有助于心脏健康。水波蛋提供完整的氨基酸谱，促进肌肉修复。',
                prep_time='15分钟', difficulty='简单', meal_type='breakfast'
            ),
            Food(
                name='蓝莓坚果酸奶碗',
                description='高蛋白免煮早餐，蓝莓的抗氧化力搭配希腊酸奶的丰富蛋白质。',
                calories=320, protein=18, carbs=35, fat=12, fiber=5,
                tags='高蛋白,免煮',
                ingredients=json.dumps([
                    {'name': '希腊酸奶', 'amount': '200g'},
                    {'name': '新鲜蓝莓', 'amount': '50g'},
                    {'name': '混合坚果', 'amount': '20g'},
                    {'name': '蜂蜜', 'amount': '1茶匙'}
                ]),
                steps=json.dumps([
                    {'title': '准备酸奶底', 'desc': '将希腊酸奶倒入碗中。'},
                    {'title': '摆盘装饰', 'desc': '撒上蓝莓和坚果，淋上蜂蜜即可。'}
                ]),
                benefits='希腊酸奶富含蛋白质和益生菌，蓝莓是天然抗氧化剂。',
                prep_time='5分钟', difficulty='简单', meal_type='breakfast'
            ),
            Food(
                name='嫩煎鸡胸肉沙拉',
                description='低GI优质蛋白午餐，鸡胸肉搭配新鲜蔬菜。',
                calories=450, protein=35, carbs=20, fat=18, fiber=8,
                tags='低GI,优质脂',
                ingredients=json.dumps([
                    {'name': '鸡胸肉', 'amount': '150g'},
                    {'name': '混合生菜', 'amount': '100g'},
                    {'name': '樱桃番茄', 'amount': '6个'},
                    {'name': '橄榄油', 'amount': '1汤匙'}
                ]),
                steps=json.dumps([
                    {'title': '煎鸡胸肉', 'desc': '鸡胸肉用盐和黑胡椒腌制，中火煎至两面金黄。'},
                    {'title': '准备沙拉', 'desc': '生菜铺底，放上切片鸡胸肉和番茄。'},
                    {'title': '调味', 'desc': '淋上橄榄油和柠檬汁即可。'}
                ]),
                benefits='鸡胸肉是优质低脂蛋白来源，搭配蔬菜提供丰富纤维。',
                prep_time='20分钟', difficulty='简单', meal_type='lunch'
            ),
            Food(
                name='柠檬香煎三文鱼配芦笋',
                description='Omega-3丰富的晚餐选择，低碳水高蛋白。',
                calories=380, protein=28, carbs=12, fat=22, fiber=4,
                tags='Omega-3,低碳水',
                ingredients=json.dumps([
                    {'name': '三文鱼排', 'amount': '150g'},
                    {'name': '芦笋', 'amount': '100g'},
                    {'name': '柠檬', 'amount': '1/2个'},
                    {'name': '橄榄油', 'amount': '1汤匙'}
                ]),
                steps=json.dumps([
                    {'title': '煎三文鱼', 'desc': '三文鱼抹盐和黑胡椒，皮面朝下煎4分钟，翻面再煎2分钟。'},
                    {'title': '烤芦笋', 'desc': '芦笋抹橄榄油，撒盐，烤箱200度烤8分钟。'},
                    {'title': '装盘', 'desc': '三文鱼和芦笋装盘，挤上柠檬汁。'}
                ]),
                benefits='三文鱼富含Omega-3脂肪酸，有助于大脑和心脏健康。',
                prep_time='15分钟', difficulty='中等', meal_type='dinner'
            ),
            Food(
                name='混合坚果与苹果片',
                description='高纤维健康加餐，补充能量。',
                calories=180, protein=5, carbs=20, fat=10, fiber=4,
                tags='高纤维',
                ingredients=json.dumps([
                    {'name': '混合坚果', 'amount': '25g'},
                    {'name': '苹果', 'amount': '1个'}
                ]),
                steps=json.dumps([
                    {'title': '准备食材', 'desc': '苹果切片，搭配混合坚果即可食用。'}
                ]),
                benefits='坚果提供健康脂肪，苹果富含膳食纤维。',
                prep_time='3分钟', difficulty='简单', meal_type='snack'
            ),
            Food(
                name='香煎鸡胸肉暖沙拉',
                description='温暖的低GI午餐，适合秋冬季节。',
                calories=450, protein=35, carbs=25, fat=18, fiber=7,
                tags='低GI,优质脂',
                ingredients=json.dumps([
                    {'name': '鸡胸肉', 'amount': '150g'},
                    {'name': '藜麦', 'amount': '50g'},
                    {'name': '西兰花', 'amount': '80g'},
                    {'name': '甜椒', 'amount': '1/2个'}
                ]),
                steps=json.dumps([
                    {'title': '煮藜麦', 'desc': '藜麦加水煮15分钟至软烂。'},
                    {'title': '煎鸡胸肉', 'desc': '鸡胸肉煎至金黄切片。'},
                    {'title': '组合', 'desc': '藜麦铺底，放上鸡胸肉和蔬菜。'}
                ]),
                benefits='藜麦是完全蛋白来源，搭配鸡胸肉蛋白质加倍。',
                prep_time='25分钟', difficulty='中等', meal_type='lunch'
            ),
        ]
        db.session.add_all(foods)

        # 创建成就数据
        achievements = [
            Achievement(name='毅力萌芽', description='连续坚持 7 天', icon='local_fire_department', color='orange', condition_type='streak', condition_value=7),
            Achievement(name='美食品鉴', description='记录 50 顿健康餐', icon='restaurant_menu', color='green', condition_type='records', condition_value=50),
            Achievement(name='健康律动', description='体重初见成效', icon='ecg_heart', color='red', condition_type='weight', condition_value=1),
            Achievement(name='内心平静', description='完成首次冥想', icon='self_improvement', color='purple', condition_type='records', condition_value=1),
            Achievement(name='百日宗师', description='坚持 100 天', icon='trophy', color='yellow', condition_type='streak', condition_value=100),
            Achievement(name='社区红人', description='获得 1000 点赞', icon='celebration', color='pink', condition_type='community', condition_value=1000),
            Achievement(name='营养专家', description='解锁所有食谱', icon='nutrition', color='teal', condition_type='records', condition_value=100),
            Achievement(name='榜上有名', description='进入排行榜前 10', icon='social_leaderboard', color='blue', condition_type='community', condition_value=10),
        ]
        db.session.add_all(achievements)

        db.session.commit()
        print('示例数据已填充')
        print('管理员账号: admin / admin123')
        print('测试账号: 林小悦 / 123456')


if __name__ == '__main__':
    init_database()
