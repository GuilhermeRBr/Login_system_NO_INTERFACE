from db.connect import returnSession
from src.models.loginModel import User
import bcrypt

session = returnSession()

def encrypt(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')


def user_registration(name, email, password):
    encrypted_password = encrypt(password)

    try:
        existent_user = session.query(User).filter_by(email=email).first()
        if existent_user:
            raise ValueError("Usuário já cadastrado com este email.")
        else:
            new_user = User(name=name, email=email, password=encrypted_password)
            session.add(new_user)
            session.commit()
            return new_user
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    