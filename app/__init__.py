from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a instância da aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/loja'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

from app import routes  # Importa as rotas