from flask import Blueprint, jsonify, request, session
from models import db
from models.user import User
from models.achievement import Achievement, UserAchievement, AIBodyData
from routes.auth_helper import get_current_user

achievement_bp = Blueprint('achievement', __name__)


@achievement_bp.route('/all', methods=['GET'])
def get_all():
    user = get_current_user()
    achievements = Achievement.query.all()

    unlocked_ids = set()
    if user:
        unlocked_ids = {ua.achievement_id for ua in UserAchievement.query.filter_by(user_id=user.id).all()}

    return jsonify([a.to_dict(unlocked=(a.id in unlocked_ids)) for a in achievements])


@achievement_bp.route('/unlocked', methods=['GET'])
def get_unlocked():
    user = get_current_user()
    if not user:
        return jsonify([])

    ua_list = UserAchievement.query.filter_by(user_id=user.id).all()
    result = []
    for ua in ua_list:
        achievement = Achievement.query.get(ua.achievement_id)
        if achievement:
            result.append(achievement.to_dict(unlocked=True))
    return jsonify(result)


@achievement_bp.route('/ai/body-data', methods=['POST'])
def submit_body_data():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401

    data = request.get_json()
    height = data.get('height', 0)
    weight = data.get('weight', 0)
    bmi = round(weight / ((height / 100) ** 2), 1) if height > 0 else 0

    body_data = AIBodyData(
        user_id=user.id,
        gender=data.get('gender', ''),
        age=data.get('age', 0),
        height=height,
        weight=weight,
        body_fat=data.get('body_fat', 0),
        bmi=bmi,
        daily_calories=data.get('dailyCalories', 1500),
        protein=data.get('protein', 95),
        carbs=data.get('carbs', 140),
        fat=data.get('fat', 45)
    )
    db.session.add(body_data)

    user.gender = data.get('gender', user.gender)
    user.age = data.get('age', user.age)
    user.height = height or user.height
    user.weight = weight or user.weight
    user.body_fat = data.get('body_fat', user.body_fat)

    db.session.commit()
    return jsonify({'success': True})


@achievement_bp.route('/ai/plan', methods=['GET'])
def get_plan():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401

    body_data = AIBodyData.query.filter_by(user_id=user.id).order_by(AIBodyData.created_at.desc()).first()

    bmi = body_data.bmi if body_data else (round(user.weight / ((user.height / 100) ** 2), 1) if user.height > 0 else 22.5)
    daily_calories = body_data.daily_calories if body_data else 1500

    return jsonify({
        'bmi': bmi,
        'dailyCalories': daily_calories,
        'macros': {
            'protein': body_data.protein if body_data else 95,
            'carbs': body_data.carbs if body_data else 140,
            'fat': body_data.fat if body_data else 45
        },
        'meals': {
            'breakfast': [
                {'name': '蓝莓坚果酸奶碗', 'calories': 320, 'protein': 18, 'tags': ['高蛋白', '免煮']},
                {'name': '牛油果水波蛋', 'calories': 345, 'protein': 18, 'tags': ['高蛋白', '低GI']}
            ],
            'lunch': [
                {'name': '香煎鸡胸肉暖沙拉', 'calories': 450, 'protein': 35, 'tags': ['低GI', '优质脂']},
                {'name': '嫩煎鸡胸肉沙拉', 'calories': 450, 'protein': 35, 'tags': ['低GI']}
            ],
            'snack': [
                {'name': '混合坚果与苹果片', 'calories': 180, 'protein': 5, 'tags': ['高纤维']}
            ],
            'dinner': [
                {'name': '柠檬香煎三文鱼配芦笋', 'calories': 380, 'protein': 28, 'tags': ['Omega-3', '低碳水']}
            ]
        }
    })


@achievement_bp.route('/ai/apply', methods=['POST'])
def apply_plan():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401

    user.plan_days = user.plan_days + 1
    db.session.commit()
    return jsonify({'success': True})
