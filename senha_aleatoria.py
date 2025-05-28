import random

def gerar_senha():
    '''
    Gera uma senha aleatória de 12 caracteres contendo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial
    '''
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = '!@#$%&*'

    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]

    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

print(f'Senha gerada: {gerar_senha()}')