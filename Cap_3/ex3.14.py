km = float(input('Quantidade de km percorridos: '))
dias = int(input('Dias alugados: '))
preco = dias * 60 + km * 0.15
print(f'Preço a pagar: R${preco:.2f}')
