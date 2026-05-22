from flask import Blueprint, request, jsonify, session
from models.food import Food

food_bp = Blueprint('food', __name__)


@food_bp.route('/<int:food_id>', methods=['GET'])
def get_detail(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({'success': False, 'message': '食物不存在'}), 404
    return jsonify(food.to_dict())


@food_bp.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '').strip()
    if not q:
        foods = Food.query.limit(20).all()
    else:
        foods = Food.query.filter(Food.name.contains(q)).limit(20).all()
    return jsonify([f.to_dict() for f in foods])


@food_bp.route('/<int:food_id>/favorite', methods=['POST'])
def toggle_favorite(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({'success': False, 'message': '食物不存在'}), 404
    return jsonify({'success': True, 'isFavorite': True})
