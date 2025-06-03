from controllers.loginController import *
from utils.validators import *

def login_screen():
    while True:
        print('Bem-vindo ao sistema de login!\n' \
            '1. Cadastrar novo usuário\n'
            '2. Fazer login\n')
        
        option = input('Escolha uma opção: ')
        if option == '1':
            name= validate_name()
            email = validate_email()
            print('A senha deve conter pelo menos 8 caracteres, incluindo letras, números e caracteres especiais:')
            password = validate_password()

            login, user = user_registration(name, email, password)
            
            if login:
                print(f'Usuário {user.name} cadastrado com sucesso!\n')
                break

        elif option == '2':
            email = input('Digite o email do usuário: ')
            senha = input('Digite a senha do usuário: ')
            usuario = session.query(User).filter_by(email=email, senha=senha).first()
            if usuario:
                print(f'Login bem-sucedido! Bem-vindo, {usuario.nome}!')
            else:
                print('Email ou senha incorretos. Tente novamente.')
        else:
            print('Opção inválida!')

    while True:
        print(f'Seja bem vindo {name}!\n')
        option = input('Digite 0 para sair: ')
        if option == '0':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente novamente.')