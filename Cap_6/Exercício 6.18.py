'''
Ex 6.18:
    Escreva um programa que gere um dicionário, onde
    cada chave seja uma caractere, e seu valor seja
    o número desse caractere encontrado em uma frase lida.
'''
dicio = {}
frase = str(input('Digite uma frase: ')).strip()
for c in frase:
    if not (c == ' '):
        dicio[c] = 1

print(dicio)
