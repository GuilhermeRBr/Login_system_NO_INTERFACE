from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

USUARIO = 'root'
SENHA = ''
HOST = 'localhost'
BANCO = 'Sistema de Login'
PORTA = '3306'

Conexao = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'

engine = create_engine(Conexao, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(50))
    senha = Column(String(60))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self.criptografar_senha(senha)

    def criptografar_senha(self, senha):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

