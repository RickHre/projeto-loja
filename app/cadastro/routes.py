from flask import render_template, request, redirect, url_for
from app import db
from app.models import Cliente
from app.cadastro import cadastro

# Cadastro de clientes
@cadastro.route('/cadastro', methods=['GET', 'POST'])
def cadastro_cliente():
    erros = None
    sucesso = None

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        if not nome or not email:
            erros = "Nome e email são obrigatórios!"
        elif Cliente.query.filter_by(email=email).first():
            erros = "E-mail já cadastrado!"
        else:
            cliente = Cliente(nome=nome, email=email, telefone=telefone)
            try:
                db.session.add(cliente)
                db.session.commit()
                sucesso = "Cliente cadastrado com sucesso!"
            except:
                db.session.rollback()
                erros = "Erro ao salvar no banco de dados!"

    return render_template('cadastro.html', erros=erros, sucesso=sucesso)

# Editar cliente
@cadastro.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nome = request.form.get('nome')
        cliente.email = request.form.get('email')
        cliente.telefone = request.form.get('telefone')

        try:
            db.session.commit()
            return redirect(url_for('main.exibir_clientes'))
        except:
            db.session.rollback()
            return "Erro ao atualizar cliente!", 500

    return render_template('editar.html', cliente=cliente)