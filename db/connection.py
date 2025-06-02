from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def retornaSession():
    USUARIO = 'root'
    SENHA = ''
    HOST = 'localhost'
    BANCO = 'Sistema de Login'
    PORTA = '3306'

    Conexao = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'
    engine = create_engine(Conexao, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()