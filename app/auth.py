from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario
from .import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Rota para a página inicial
@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('cliente.listar_clientes'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = Usuario.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('cliente.listar_clientes'))
        else:
            flash('Email ou senha inválidos.', 'danger')
            return render_template('login.html')

    return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('cliente.listar_clientes'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('Este email já está cadastrado.', 'error')
            return render_template('cadastro.html')

        if password != confirm_password:
            flash('As senhas não coincidem.', 'error')
            return render_template('cadastro.html')

        if Usuario.pode_cadastrar(): # Verifica se pode cadastrar mais usuários
            new_user = Usuario(username=username, email=email, password=password) # Temporariamente armazenando a senha em texto plano
            new_user.set_password(password) # Hashing da senha antes de salvar
            db.session.add(new_user)
            db.session.commit()
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('O número máximo de usuários cadastrados foi atingido.', 'warning')
            return render_template('cadastro.html')

    return render_template('cadastro.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso.', 'info')
    return redirect(url_for('auth.login'))