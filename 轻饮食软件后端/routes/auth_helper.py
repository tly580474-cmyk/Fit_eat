from flask import request, session
from models.user import User


def get_current_user():
    """获取当前登录用户，支持 session 和 Bearer token 两种认证方式"""
    # 优先从 session 获取
    user_id = session.get('user_id')
    if user_id:
        return User.query.get(user_id)
    # Fallback: 从 Authorization header 获取 Bearer token
    auth_header = request.headers.get('Authorization', '')
    if auth_header.startswith('Bearer '):
        token = auth_header[7:]
        if token.startswith('user_'):
            try:
                user_id = int(token[5:])
                return User.query.get(user_id)
            except ValueError:
                pass
    return None
