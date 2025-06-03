import re


def validate_name():
    while True:
        name = input('NOME: ')
        if not name.strip():
            print("Nome não pode ser vazio.")
        elif not re.match(r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$", name):
            print("Nome inválido.")
        else:
            return name.title()

def validate_email():
    while True:
        email = input('EMAIL: ')
        if not email.strip():
            print("Email não pode ser vazio.")
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    , email):
            print("Email inválido.")
        else:
            return email.lower()

def validate_password():
    while True:
        password = input('SENHA: ')
        if not password.strip():
            print("Senha não pode ser vazia.")
        elif len(password) < 8:
            print("Senha deve ter no mínimo 8 caracteres.")
        elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[\W_]).{8,}$', password):
            print("Senha muita fraca! Ela deve conter pelo menos uma letra, um número e um caractere especial.")
        else:
            return password