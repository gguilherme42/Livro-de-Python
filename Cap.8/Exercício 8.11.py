'''
Ex. 8.11:
    Escreva uma função para validar uma variável string.
    Essa função recebe como parâmetro a string, o número mínimo e
    máximo de caracteres. Retorne verdadeiro e se o tamanho da string
    estiver entre os valores de máximo e mínimo, falso em casa contrário
'''


def valid(msg='', min=0, max=100):
    if max >= len(msg) >= min:
        return True
    else:
        return False

while True:
    f = str(input('Digite uma frase: ')).strip()
    print(valid(f, 1, 10))
