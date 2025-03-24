from flask import render_template, redirect, url_for
from app.models import Cliente
from app.main import main
from app import db
from flask import request

#temp
@main.route('/teste')
def teste():
    return render_template('base.html')  # Testa se o Flask localiza o base.html

import os
@main.route('/')
def index():
    return render_template(os.path.abspath("app/main/templates/index.html"))

# Página inicial
@main.route('/')
def index():
    return render_template('index.html')

# Listagem de clientes
@main.route('/clientes', methods=['GET'])
def exibir_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

# Editar cliente
@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        # Atualiza os dados do cliente com base no formulário enviado
        cliente.nome = request.form.get('nome')
        cliente.email = request.form.get('email')
        cliente.telefone = request.form.get('telefone')

        try:
            db.session.commit()
            return redirect(url_for('main.exibir_clientes'))
        except:
            db.session.rollback()
            return "Erro ao atualizar cliente!", 500

    # Renderiza o template de edição com os dados do cliente
    return render_template('editar.html', cliente=cliente)

# Excluir cliente
@main.route('/excluir/<int:id>', methods=['GET'])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    try:
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('main.exibir_clientes'))
    except:
        db.session.rollback()
        return "Erro ao excluir cliente!", 500