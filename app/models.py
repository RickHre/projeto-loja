from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'acesso'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'
    @classmethod
    def pode_cadastrar(cls):
        """Verifica se o número total de usuários cadastrados permite um novo cadastro."""
        LIMITE_DE_USUARIOS = 4
        total_usuarios = cls.query.count()
        return total_usuarios < LIMITE_DE_USUARIOS

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    cidade = db.Column(db.String(80))

    def __repr__(self):
        return f'<Cliente {self.nome_completo}>'