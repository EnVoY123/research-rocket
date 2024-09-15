import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/flask_auth_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = Config()