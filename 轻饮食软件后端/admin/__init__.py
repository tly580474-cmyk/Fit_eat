from flask_admin import Admin
from flask_login import current_user
from flask import redirect, url_for


def init_admin(app, db):
    from admin.views import (
        UserModelView, FoodModelView, DietRecordModelView,
        WaterRecordModelView, CommunityPostModelView,
        CommentModelView, AchievementModelView,
        UserAchievementModelView, AIBodyDataModelView
    )
    from models.user import User
    from models.food import Food
    from models.diet import DietRecord, WaterRecord
    from models.community import CommunityPost, Comment, Like, Follow
    from models.achievement import Achievement, UserAchievement, AIBodyData

    admin = Admin(
        app,
        name='轻饮食管理后台',
        template_mode='bootstrap4',
        url='/admin'
    )

    admin.add_view(UserModelView(User, db.session, name='用户管理'))
    admin.add_view(FoodModelView(Food, db.session, name='食物库'))
    admin.add_view(DietRecordModelView(DietRecord, db.session, name='饮食记录'))
    admin.add_view(WaterRecordModelView(WaterRecord, db.session, name='饮水记录'))
    admin.add_view(CommunityPostModelView(CommunityPost, db.session, name='社区动态'))
    admin.add_view(CommentModelView(Comment, db.session, name='评论管理'))
    admin.add_view(AchievementModelView(Achievement, db.session, name='成就管理'))
    admin.add_view(UserAchievementModelView(UserAchievement, db.session, name='用户成就'))
    admin.add_view(AIBodyDataModelView(AIBodyData, db.session, name='AI身体数据'))

    return admin
