from app import app, db
from flask import request, jsonify, render_template
from app.models import Cliente

@app.route('/')
def index():
    return "Bem-vindo ao sistema de cadastro de clientes!"

@app.route('/cadastro', methods=['POST'])
def cadastro_cliente():
    if request.content_type == 'application/json':
        # Caso os dados sejam enviados como JSON
        dados = request.json
        nome = dados['nome']
        email = dados['email']
        telefone = dados['telefone']
    else:
        # Caso os dados sejam enviados via formulário HTML
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

    # Verifica se o e-mail já existe
    cliente_existente = Cliente.query.filter_by(email=email).first()
    if cliente_existente:
        return jsonify({"erro": "E-mail já cadastrado!"}), 400

    # Adiciona o cliente ao banco de dados
    cliente = Cliente(nome=nome, email=email, telefone=telefone)
    db.session.add(cliente)
    db.session.commit()

    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"})

@app.route('/formulario', methods=['GET'])
def formulario_cliente():
    return render_template('cadastro.html')