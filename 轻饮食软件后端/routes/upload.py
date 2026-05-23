import os
import uuid
from datetime import datetime
from flask import Blueprint, request, jsonify, session, current_app
from models.user import User

upload_bp = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return None
    return User.query.get(user_id)


@upload_bp.route('/image', methods=['POST'])
def upload_image():
    user = get_current_user()
    if not user:
        return jsonify({'success': False, 'message': '未登录'}), 401

    if 'file' not in request.files:
        return jsonify({'success': False, 'message': '没有文件'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': '未选择文件'}), 400

    if not allowed_file(file.filename):
        return jsonify({'success': False, 'message': '不支持的文件格式'}), 400

    # 生成唯一文件名
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}_{int(datetime.now().timestamp())}.{ext}"

    # 确保上传目录存在
    upload_dir = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_dir, exist_ok=True)

    # 保存文件
    filepath = os.path.join(upload_dir, filename)
    file.save(filepath)

    # 返回可访问的URL
    image_url = f"/api/uploads/{filename}"

    return jsonify({
        'success': True,
        'url': image_url,
        'filename': filename
    })
