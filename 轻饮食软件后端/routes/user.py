from flask import Blueprint, request, jsonify, session
from models import db
from models.user import User

user_bp = Blueprint('user', __name__)


def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return None
    return User.query.get(user_id)


@user_bp.route('/profile', methods=['GET'])
def get_profile():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401
    return jsonify(user.to_dict())


@user_bp.route('/profile', methods=['PUT'])
def update_profile():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'avatar' in data:
        user.avatar = data['avatar']
    if 'bio' in data:
        user.bio = data['bio']
    if 'gender' in data:
        user.gender = data['gender']
    if 'age' in data:
        user.age = data['age']
    if 'height' in data:
        user.height = data['height']
    if 'weight' in data:
        user.weight = data['weight']
    if 'body_fat' in data:
        user.body_fat = data['body_fat']
    if 'target_weight' in data:
        user.target_weight = data['target_weight']
    if 'target_calories' in data:
        user.target_calories = data['target_calories']

    db.session.commit()
    return jsonify({'success': True, 'data': user.to_dict()})
