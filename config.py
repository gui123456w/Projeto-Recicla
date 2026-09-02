import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# .env é usado no desenvolvimento local.
# No Render, os valores vêm das Environment Variables.
load_dotenv()


class Config:
    # ==========================================
    # FLASK
    # ==========================================
    SECRET_KEY = os.getenv("SECRET_KEY")

    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY não configurada.")

    # ==========================================
    # BANCO DE DADOS
    # ==========================================
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME")

    if not DB_HOST:
        raise RuntimeError("DB_HOST não configurada.")

    if not DB_USER:
        raise RuntimeError("DB_USER não configurada.")

    if not DB_NAME:
        raise RuntimeError("DB_NAME não configurada.")

    DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{DB_USER}:"
        f"{DB_PASSWORD_ENCODED}@"
        f"{DB_HOST}:"
        f"{DB_PORT}/"
        f"{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================================
    # E-MAIL
    # ==========================================
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # ==========================================
    # UPLOADS
    # ==========================================
    UPLOAD_FOLDER = "static/arquivo_tarefa"