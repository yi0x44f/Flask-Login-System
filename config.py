from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv(override=True)  # 載入 .env


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # Flask secret key for CSRF protection and session management
    SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")
    # JWT secret key for encoding and decoding tokens
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)  # Access token expiration time

