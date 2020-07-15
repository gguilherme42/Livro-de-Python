soma = lambda x, y: x + y
div = lambda x, y: x / y
sub = lambda x, y: x - y
mult = lambda x, y: x * y
a, b = int(input('Número: ')), int(input('Número: '))
print(''' 1 - Soma
2 - Subtração
3 - Divisão
4 - Multiplicação
''')
resp = int(input('Digite um operação: '))
if resp == 1:
    print(f'Soma: {soma(a, b)}')
elif resp == 2:
    print(f'Subtração: {sub(a, b)}')
elif resp == 3:
    print(f'Divisão: {div(a, b):.1f}')
elif resp == 4:
    print(f'Multiplicação: {mult(a, b)}')
else:
    print('Operação inválida!')


