c = float(input('Valor inicial da dívida: R$'))
i = float(input('Juros mensal: '))
pagar = float(input('Valor mensal pago: R$'))
t = c // pagar
j = c * i * t
m = c + j
print(f'''Número de meses da dívida: {t}
Total pago: {m}
Total de juros: {j}''')

