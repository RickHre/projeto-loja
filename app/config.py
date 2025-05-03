import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_segura_padrao'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///./instance/lojaP2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False