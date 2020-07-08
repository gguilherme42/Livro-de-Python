preco = float(input('Valor da mercadoria: R$'))
desc = float(input('Valor do desconto (ex.: 10%): '))
valorDesc = preco * desc / 100
valorfinal = preco - valorDesc
print(f'''Valor do desconto: R${valorDesc:.2f}
Valor da mercadoria: R${valorfinal:.2f}''')
