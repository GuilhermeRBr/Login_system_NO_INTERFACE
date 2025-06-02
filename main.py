from src.controllers.loginController import *

while True:
    print('Bem-vindo ao sistema de login!\n' \
        '1. Cadastrar novo usuário\n'
        '2. Fazer login\n')
    
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        nome = 'laura'
        email = 'gui@gmail.com'
        senha = '34322'

        cadastrar_usuario(nome, email, senha)

    elif opcao == '2':
        email = input('Digite o email do usuário: ')
        senha = input('Digite a senha do usuário: ')
        usuario = session.query(Usuario).filter_by(email=email, senha=senha).first()
        if usuario:
            print(f'Login bem-sucedido! Bem-vindo, {usuario.nome}!')
        else:
            print('Email ou senha incorretos. Tente novamente.')
    else:
        print('Opção inválida!')
    