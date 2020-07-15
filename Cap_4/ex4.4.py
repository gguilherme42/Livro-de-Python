sal = float(input('Salário: R$ '))
m = 10 if sal > 1250 else 15
a = sal * m / 100
print(f'Valor do aumento: R${a:.2f}')
