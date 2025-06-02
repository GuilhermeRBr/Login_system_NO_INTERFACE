from src.controllers.loginController import *

while True:
    print('Bem-vindo ao sistema de login!\n' \
        '1. Cadastrar novo usuário\n'
        '2. Fazer login\n')
    
    option = input('Escolha uma opção: ')
    if option == '1':
        name= 'laura'
        email = 'gui@gmail.com'
        password = '34322'

        user_registration(name, email, password)

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
    