from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('config.Config')  # Carrega as configurações

    db.init_app(app)

    # Importa e registra os Blueprints
    from app.main import main as main_blueprint
    from app.cadastro import cadastro as cadastro_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(cadastro_blueprint)

    return app