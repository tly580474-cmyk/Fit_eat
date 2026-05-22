import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'light-diet-secret-key-2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'light_diet.db').replace('\\', '/')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
