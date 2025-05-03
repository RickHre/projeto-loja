from flask import Blueprint, render_template, request, redirect, url_for, flash

from datetime import date

cliente_bp = Blueprint('cliente', __name__, url_prefix='/clientes')
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Rotas para o Blueprint de Cliente
@cliente_bp.route('/')
def listar_clientes():
    from .models import Cliente, db
    search_term = request.args.get('search_term')
    clientes = Cliente.query.all()

    if search_term:
        search_term = search_term.lower()
        clientes = [
            cliente for cliente in clientes
            if search_term in cliente.nome_completo.lower() or
               search_term in cliente.email.lower() or
               search_term in cliente.cpf.lower() or
               search_term in cliente.telefone.lower() or
               search_term in str(cliente.id).lower()
        ]

    return render_template('clientes.html', clientes=clientes)

@cliente_bp.route('/novo')
def novo_cliente():
    return render_template('novoCliente.html')

@cliente_bp.route('/editar/<int:cliente_id>')
def editar_cliente(cliente_id):
    from .models import Cliente, db
    cliente = Cliente.query.get_or_404(cliente_id)
    return render_template('editar.html', cliente=cliente)

@cliente_bp.route('/excluir/<int:cliente_id>')
def excluir_cliente(cliente_id):
    from .models import Cliente, db
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente.listar_clientes'))

# Rotas para salvar os dados do novo cliente e da edição
@cliente_bp.route('/salvar', methods=['POST'])
def salvar_cliente():
    nome_completo = request.form['nome_completo']
    email = request.form['email']
    nascimento_str = request.form['nascimento']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    rua = request.form['rua']
    numero = request.form['numero']
    cidade = request.form['cidade']

    try:
        nascimento = date.fromisoformat(nascimento_str)
    except ValueError:
        flash('Formato de data inválido.', 'danger')
        return redirect(url_for('cliente.novo_cliente'))

    # Verificar se o CPF já existe no banco de dados
    from .models import Cliente, db
    cliente_existente_cpf = Cliente.query.filter_by(cpf=cpf).first()
    if cliente_existente_cpf:
        flash('CPF já cadastrado para outro cliente.', 'warning')
        return redirect(url_for('cliente.novo_cliente'))

    # Verificar se o email já existe no banco de dados
    cliente_existente_email = Cliente.query.filter_by(email=email).first()
    if cliente_existente_email:
        flash('Email já cadastrado para outro cliente.', 'warning')
        return redirect(url_for('cliente.novo_cliente'))

    novo_cliente = Cliente(
        nome_completo=nome_completo,
        email=email,
        nascimento=nascimento,
        cpf=cpf,
        telefone=telefone,
        rua=rua,
        numero=numero,
        cidade=cidade
    )

    db.session.add(novo_cliente)
    db.session.commit()
    flash('Cliente cadastrado com sucesso!', 'success')
    return redirect(url_for('cliente.listar_clientes'))

@cliente_bp.route('/atualizar/<int:cliente_id>', methods=['POST'])
def atualizar_cliente(cliente_id):
    from .models import Cliente, db

    # Buscar o cliente no banco de dados
    cliente = Cliente.query.get_or_404(cliente_id)

    # Obter os dados do formulário
    nome_completo = request.form.get('nome_completo')
    email = request.form.get('email')
    cpf = request.form.get('cpf')
    data_nascimento_str = request.form.get('nascimento')
    telefone = request.form.get('telefone')
    rua = request.form.get('rua')
    numero = request.form.get('numero')
    cidade = request.form.get('cidade')

    # Verificar campos obrigatórios
    if not nome_completo or not email or not cpf:
        flash('Nome completo, email e CPF são obrigatórios.', 'danger')
        return redirect(url_for('cliente.editar_cliente', cliente_id=cliente_id))

    # Verificar se o novo email já existe para outro cliente
    outro_cliente_com_email = Cliente.query.filter(Cliente.email == email, Cliente.id != cliente.id).first()
    if outro_cliente_com_email:
        flash('Este email já está cadastrado para outro cliente.', 'warning')
        return redirect(url_for('cliente.editar_cliente', cliente_id=cliente_id))

    # Verificar se o novo CPF já existe para outro cliente
    outro_cliente_com_cpf = Cliente.query.filter(Cliente.cpf == cpf, Cliente.id != cliente.id).first()
    if outro_cliente_com_cpf:
        flash('Este CPF já está cadastrado para outro cliente.', 'warning')
        return redirect(url_for('cliente.editar_cliente', cliente_id=cliente_id))

    # Atualizar os dados do cliente
    cliente.nome_completo = nome_completo
    cliente.email = email
    cliente.cpf = cpf
    cliente.telefone = telefone
    cliente.rua = rua
    cliente.numero = numero
    cliente.cidade = cidade

    # Validar e atualizar a data de nascimento
    try:
        cliente.nascimento = date.fromisoformat(data_nascimento_str)
    except ValueError:
        flash('Data de nascimento inválida. Use o formato AAAA-MM-DD.', 'danger')
        return redirect(url_for('cliente.editar_cliente', cliente_id=cliente_id))

    # Salvar as alterações no banco de dados
    db.session.commit()
    flash('Cliente atualizado com sucesso!', 'success')
    return redirect(url_for('cliente.listar_clientes'))

# Rotas para o Blueprint de Autenticação
@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@auth_bp.route('/login', methods=['POST'])
def fazer_login():
    return 'Fazendo login...'

@auth_bp.route('/cadastro', methods=['POST'])
def registrar_usuario():
    return 'Registrando usuário...'

@auth_bp.route('/logout')
def logout():
    return 'Deslogando usuário...'