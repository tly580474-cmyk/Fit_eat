from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for


class BaseAdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.index'))


class UserModelView(BaseAdminView):
    column_list = ['id', 'username', 'email', 'gender', 'age', 'height', 'weight', 'target_calories', 'plan_days', 'created_at']
    column_searchable_list = ['username', 'email']
    column_filters = ['gender', 'created_at']
    column_labels = {
        'username': '用户名', 'email': '邮箱', 'gender': '性别',
        'age': '年龄', 'height': '身高', 'weight': '体重',
        'target_calories': '目标热量', 'plan_days': '计划天数', 'created_at': '注册时间'
    }
    can_export = True

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_user', **kwargs)


class FoodModelView(BaseAdminView):
    column_list = ['id', 'name', 'calories', 'protein', 'carbs', 'fat', 'meal_type', 'difficulty']
    column_searchable_list = ['name']
    column_filters = ['meal_type', 'difficulty']
    column_labels = {
        'name': '名称', 'calories': '热量', 'protein': '蛋白质',
        'carbs': '碳水', 'fat': '脂肪', 'meal_type': '餐类', 'difficulty': '难度'
    }
    can_export = True

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_food', **kwargs)


class DietRecordModelView(BaseAdminView):
    column_list = ['id', 'user_id', 'food_name', 'meal_type', 'calories', 'protein', 'amount', 'recorded_at']
    column_searchable_list = ['food_name']
    column_filters = ['meal_type', 'recorded_at']
    column_labels = {
        'user_id': '用户ID', 'food_name': '食物', 'meal_type': '餐类',
        'calories': '热量', 'protein': '蛋白质', 'amount': '份量', 'recorded_at': '记录时间'
    }
    can_export = True

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_diet', **kwargs)


class WaterRecordModelView(BaseAdminView):
    column_list = ['id', 'user_id', 'amount', 'recorded_at']
    column_filters = ['recorded_at']
    column_labels = {'user_id': '用户ID', 'amount': '饮水量(ml)', 'recorded_at': '记录时间'}

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_water', **kwargs)


class CommunityPostModelView(BaseAdminView):
    column_list = ['id', 'user_id', 'content', 'location', 'category', 'created_at']
    column_searchable_list = ['content']
    column_filters = ['category', 'created_at']
    column_labels = {
        'user_id': '用户ID', 'content': '内容', 'location': '位置',
        'category': '分类', 'created_at': '发布时间'
    }

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_post', **kwargs)


class CommentModelView(BaseAdminView):
    column_list = ['id', 'post_id', 'user_id', 'content', 'created_at']
    column_searchable_list = ['content']
    column_labels = {
        'post_id': '动态ID', 'user_id': '用户ID', 'content': '内容', 'created_at': '评论时间'
    }

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_comment', **kwargs)


class AchievementModelView(BaseAdminView):
    column_list = ['id', 'name', 'description', 'icon', 'color', 'condition_type', 'condition_value']
    column_searchable_list = ['name']
    column_labels = {
        'name': '名称', 'description': '描述', 'icon': '图标',
        'color': '颜色', 'condition_type': '条件类型', 'condition_value': '条件值'
    }

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_achievement', **kwargs)


class UserAchievementModelView(BaseAdminView):
    column_list = ['id', 'user_id', 'achievement_id', 'unlocked_at']
    column_labels = {'user_id': '用户ID', 'achievement_id': '成就ID', 'unlocked_at': '解锁时间'}

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_user_achievement', **kwargs)


class AIBodyDataModelView(BaseAdminView):
    column_list = ['id', 'user_id', 'gender', 'age', 'height', 'weight', 'bmi', 'daily_calories', 'created_at']
    column_labels = {
        'user_id': '用户ID', 'gender': '性别', 'age': '年龄',
        'height': '身高', 'weight': '体重', 'bmi': 'BMI',
        'daily_calories': '日热量', 'created_at': '记录时间'
    }
    can_export = True

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, endpoint='admin_ai_body', **kwargs)
