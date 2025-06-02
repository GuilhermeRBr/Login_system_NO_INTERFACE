from db.connect import retornaSession
from src.models.loginModel import Usuario
import bcrypt

session = retornaSession()

def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')


def cadastrar_usuario(nome, email, senha):
    senha_criptografada = criptografar_senha(senha)

    try:
        usuario_existente = session.query(Usuario).filter_by(email=email).first()
        if usuario_existente:
            raise ValueError("Usuário já cadastrado com este email.")
        else:
            novo_usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
            session.add(novo_usuario)
            session.commit()
            return novo_usuario
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    