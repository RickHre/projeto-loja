from app import app, db
from flask import request, jsonify, render_template, redirect, url_for
from app.models import Cliente

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template index.html

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_cliente():
    erros = None
    sucesso = None

    if request.method == 'POST':
        # Coleta os dados enviados pelo formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        # Validações de entrada
        if not nome or not email:
            erros = "Nome e email são obrigatórios!"
        elif Cliente.query.filter_by(email=email).first():
            erros = "E-mail já cadastrado!"
        else:
            # Adiciona o cliente ao banco de dados
            cliente = Cliente(nome=nome, email=email, telefone=telefone)
            try:
                db.session.add(cliente)
                db.session.commit()
                sucesso = "Cliente cadastrado com sucesso!"
            except Exception as e:
                db.session.rollback()
                erros = "Erro ao salvar no banco de dados!"

    # Renderiza o template, exibindo erros ou mensagens de sucesso
    return render_template('cadastro.html', erros=erros, sucesso=sucesso)

# Rota para redirecionar caso acessem a URL de '/formulario' (opcional)
@app.route('/formulario', methods=['GET'])
def redireciona_para_cadastro():
    return redirect(url_for('formulario_cliente'))  # Redireciona para a rota correta

@app.route('/clientes', methods=['GET'])
def exibir_clientes():
    # Consulta todos os clientes cadastrados
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/excluir/<int:id>', methods=['GET'])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)  # Busca o cliente ou retorna 404
    try:
        db.session.delete(cliente)  # Remove o cliente
        db.session.commit()
        return redirect(url_for('exibir_clientes'))  # Redireciona para a lista de clientes
    except Exception as e:
        db.session.rollback()
        return "Erro ao excluir cliente!", 500
    
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)  # Busca o cliente ou retorna 404
    if request.method == 'POST':
        # Atualiza os dados do cliente
        cliente.nome = request.form.get('nome')
        cliente.email = request.form.get('email')
        cliente.telefone = request.form.get('telefone')
        
        try:
            db.session.commit()
            return redirect(url_for('exibir_clientes'))  # Redireciona para a lista de clientes
        except Exception as e:
            db.session.rollback()
            return "Erro ao atualizar cliente!", 500

    # Exibe o formulário preenchido com os dados do cliente
    return render_template('editar.html', cliente=cliente)