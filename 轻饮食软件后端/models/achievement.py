from datetime import datetime
from models import db


class Achievement(db.Model):
    __tablename__ = 'achievements'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), default='')
    icon = db.Column(db.String(50), default='star')
    color = db.Column(db.String(20), default='green')
    condition_type = db.Column(db.String(50), default='')  # streak/records/weight/community
    condition_value = db.Column(db.Integer, default=0)

    def to_dict(self, unlocked=False):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.description,
            'icon': self.icon,
            'color': self.color,
            'unlocked': unlocked,
        }

    def __repr__(self):
        return f'<Achievement {self.name}>'


class UserAchievement(db.Model):
    __tablename__ = 'user_achievements'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    achievement_id = db.Column(db.Integer, db.ForeignKey('achievements.id'), nullable=False)
    unlocked_at = db.Column(db.DateTime, default=datetime.utcnow)

    achievement = db.relationship('Achievement')

    __table_args__ = (db.UniqueConstraint('user_id', 'achievement_id'),)


class AIBodyData(db.Model):
    __tablename__ = 'ai_body_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    gender = db.Column(db.String(10), default='')
    age = db.Column(db.Integer, default=0)
    height = db.Column(db.Float, default=0)
    weight = db.Column(db.Float, default=0)
    body_fat = db.Column(db.Float, default=0)
    bmi = db.Column(db.Float, default=0)
    daily_calories = db.Column(db.Integer, default=1500)
    protein = db.Column(db.Integer, default=95)
    carbs = db.Column(db.Integer, default=140)
    fat = db.Column(db.Integer, default=45)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'bmi': self.bmi,
            'dailyCalories': self.daily_calories,
            'macros': {
                'protein': self.protein,
                'carbs': self.carbs,
                'fat': self.fat,
            }
        }
