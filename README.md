# Loja Flask

Uma aplicação web desenvolvida em Flask para gerenciar clientes, incluindo funcionalidades como cadastro, edição, exclusão e listagem de clientes.

## 📋 Funcionalidades

- **Autenticação**: Login e logout de usuários.
- **Gerenciamento de Clientes**:
  - Cadastro de novos clientes.
  - Edição de informações de clientes existentes.
  - Exclusão de clientes.
  - Pesquisa de clientes por nome, email, CPF ou telefone.
- **Interface Amigável**: Utiliza templates HTML com herança e estilização com CSS.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite/MySQL
- **Frontend**: HTML, CSS, Bootstrap e SweetAlert2
- **Migrações**: Flask-Migrate
- **Autenticação**: Flask-Login

---

## 📦 Estrutura do Projeto
# Estrutura do Projeto

# Estrutura do Projeto

loja_flask/
├── app/                         # Diretório principal da aplicação
│   ├── __init__.py              # Inicializa o pacote 'app'
│   ├── config.py                # Configurações da aplicação
│   ├── models.py                # Modelos do banco de dados (SQLAlchemy)
│   ├── routes.py                # Definição das rotas da aplicação (Blueprints)
│   ├── auth.py                  # Rotas e lógica de autenticação (Blueprint)
│   ├── templates/               # Arquivos HTML para renderização
│   │   └── ...                  # Outros templates
│   ├── static/                  # Arquivos estáticos (CSS, JS, imagens)
│   │   └── ...                  # Outros arquivos estáticos
│   └── migrations/              # Scripts de migração do banco de dados (Alembic)
│       ├── versions/            # Versões das migrações
│       └── alembic.ini          # Configuração do Alembic
├── venv/                        # Ambiente virtual com as dependências instaladas
├── wsgi.py                      # Arquivo para deploy (usado no Render)
├── .flaskenv                    # Configuração do Flask CLI
├── requirements.txt             # Lista de dependências do projeto
└── app.py                       # Ponto de entrada da aplicação (pode instanciar a 'app')

---

## 🚀 Como Executar o Projeto

### 1. **Pré-requisitos**
Certifique-se de ter o Python 3.8+ instalado em sua máquina. Você pode verificar a versão instalada com:
```bash
python --version

2. Clonar o Repositório
Clone este repositório para sua máquina local:

git clone https://github.com/RickHre/projeto-loja.git
cd projeto-loja

3. Criar um Ambiente Virtual
Crie e ative um ambiente virtual:

python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

4. Instalar Dependências
Instale as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt

5. Configurar o Banco de Dados
Inicialize o banco de dados e aplique as migrações:

flask db upgrade

6. Executar a Aplicação
Inicie o servidor Flask:

py app.py

Acesse a aplicação no navegador em: http://127.0.0.1:5000

🐛 Problemas Conhecidos
Certifique-se de que o banco de dados foi inicializado corretamente antes de executar a aplicação.
Mensagens de erro detalhadas estão habilitadas no modo de depuração (debug=True).

✨ Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests

📞 Contato
Autor: Carlos Henrique
Email: hrerick30@gmail.com
GitHub: https://github.com/RickHre
