from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from . import routes
    from .auth import auth_bp
    app.register_blueprint(routes.cliente_bp)
    app.register_blueprint(auth_bp)

    from .models import Usuario  # Importe os modelos

    # Configure o user_loader DENTRO do contexto da aplicação
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    return app