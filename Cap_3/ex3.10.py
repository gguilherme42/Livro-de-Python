salario = float(input('Valor do salário: R$'))
aumento = float(input('Valor do aumento (ex.: 5%): '))
r = salario * aumento / 100
salfinal = salario + aumento
print(f'''Valor do aumento:  R${r:.2f}
→ Salário final: R${salfinal:.2f}''')
