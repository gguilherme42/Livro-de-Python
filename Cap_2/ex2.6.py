salario = float(input('Valor do salário: R$'))
aumento = float(input('Valor do aumento (ex.: 5%): '))
r = salario * aumento / 100
salfinal = salario + aumento
print(f'''Salário: R${salario:.2f}
Aumento:  {aumento:.1f}%
→ Salário final: R${salfinal:.2f}''')
