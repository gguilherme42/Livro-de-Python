'''
Ex. 5.26:
    Escreva um programa que calcule o resto da divisão inteira
    entre dois números. Utilize apenas as operações de soma e
    subtração para calcular o resultado.
'''

d = int(input('Digite o dividendo: '))
div = int(input('Digite o divisor: '))
r = 0
r1 = d // div
while div <= d:
    d -= div
    r += 1

print(f'Verificação r = {r}, v = {r1}')
