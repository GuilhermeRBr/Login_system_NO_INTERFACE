from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    senha = Column(String(30))

class Login:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha