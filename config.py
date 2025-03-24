class Config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/loja'  # Conexão com o banco MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa notificações desnecessárias do SQLAlchemy