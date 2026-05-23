import os
from flask import Flask, send_from_directory
from flask_login import LoginManager
from flask_cors import CORS
from config import Config
from models import db
from models.user import User


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    # 确保上传目录存在
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    CORS(app, supports_credentials=True)

    # Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 注册路由
    from routes import register_routes
    register_routes(app)

    # 注册 Admin 后台
    from admin import init_admin
    init_admin(app, db)

    # 前端静态文件服务
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '轻饮食软件前端')

    @app.route('/')
    def serve_index():
        return send_from_directory(frontend_dir, 'index.html')

    @app.route('/pages/<path:filename>')
    def serve_pages(filename):
        return send_from_directory(os.path.join(frontend_dir, 'pages'), filename)

    @app.route('/css/<path:filename>')
    def serve_css(filename):
        return send_from_directory(os.path.join(frontend_dir, 'css'), filename)

    @app.route('/js/<path:filename>')
    def serve_js(filename):
        return send_from_directory(os.path.join(frontend_dir, 'js'), filename)

    # 上传文件服务
    @app.route('/api/uploads/<path:filename>')
    def serve_upload(filename):
        upload_dir = app.config['UPLOAD_FOLDER']
        return send_from_directory(upload_dir, filename)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
