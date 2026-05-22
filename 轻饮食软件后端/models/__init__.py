from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.food import Food
from models.diet import DietRecord, WaterRecord
from models.community import CommunityPost, Comment, Like, Follow
from models.achievement import Achievement, UserAchievement, AIBodyData
