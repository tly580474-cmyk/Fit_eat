from routes.auth import auth_bp
from routes.user import user_bp
from routes.diet import diet_bp
from routes.food import food_bp
from routes.community import community_bp
from routes.achievement import achievement_bp


def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(diet_bp, url_prefix='/api/diet')
    app.register_blueprint(food_bp, url_prefix='/api/food')
    app.register_blueprint(community_bp, url_prefix='/api/community')
    app.register_blueprint(achievement_bp, url_prefix='/api/achievement')
