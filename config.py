from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Configuração base
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Define um valor padrão caso não seja definido no .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:@localhost/loja')  # Valor padrão
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa notificações desnecessárias do SQLAlchemy

class DevelopmentConfig(Config):
    # Configuração para ambiente de desenvolvimento
    DEBUG = True

class ProductionConfig(Config):
    # Configuração para produção (possivelmente sem DEBUG ativado)
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI', 'mysql+mysqlconnector://usuario:senha@servidor/loja_prod')

class TestingConfig(Config):
    # Configuração para ambiente de teste
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True