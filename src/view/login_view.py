from controllers.loginController import *
from utils.validators import *

def login_screen():
    while True:
        print('Bem-vindo ao sistema de login!\n' \
            '1. Cadastrar novo usuário\n'
            '2. Fazer login\n')
        
        option = input('Escolha uma opção: ')
        if option == '1':
            name = validate_name()
            email = validate_email()
            print('A senha deve conter pelo menos 8 caracteres, incluindo letras, números e caracteres especiais:')
            while True:
                password = validate_password()
                print('Confirme sua senha:')
                check_password = validate_password()
                if password == check_password:
                    break
                else:
                    print('As senhas não coincidem. Tente novamente.')

            login, user = user_registration(name, email, password)
            
            if login:
                print(f'Usuário {user.name} cadastrado com sucesso!\n')
                break

        elif option == '2':
            email = validate_email()
            password = validate_password()

            login, user = user_login(email, password)

            if login:
                print(f'Login bem-sucedido!')
                break
            else:
                print('Email ou senha incorretos. Tente novamente.')
        else:
            print('Opção inválida!')

    while True:
        print(f'Seja bem vindo {user.name}!\n')
        option = input('Digite 0 para sair: ')
        if option == '0':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente novamente.')