from flask import Blueprint

cadastro = Blueprint('cadastro', __name__)

from app.cadastro import routes