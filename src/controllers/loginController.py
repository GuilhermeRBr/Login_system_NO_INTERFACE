from db.connect import returnSession
from models.loginModel import User
import bcrypt

session = returnSession()

def encrypt(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


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
            return True, session.query(User).filter_by(email=email).first()
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    
def user_login(email, password):
    try:
        user = session.query(User).filter_by(email=email).first()
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return True, user
            else:
                return False, None
        else:
            return False, None
    except Exception as e:
        print(f"Erro: {e}")
        return False, None