mult = lambda a, b: a * b
classificacao_energia = {'R': [0.4, 0.65],
                        'I': [0.55, 0.6],
                        'C': [0.55, 0.6]}
kwh = float(input('Quantidade de KWh consumida: '))
instalacao = str(input('''Tipo de instalação:
* Digite R para Residencial
* Digite C para Comercial
* Digite I para Industrial 
''')).strip().upper()[0]
if instalacao == 'R':
    preco = mult(kwh, classificacao_energia['R'][0]) if kwh <= 500 else mult(kwh, classificacao_energia['R'][1])
    print(f'Preço: R${preco:.2f}')
elif instalacao == 'C':
    preco = mult(kwh, classificacao_energia['C'][0]) if kwh <= 1000 else mult(kwh, classificacao_energia['C'][1])
    print(f'Preço: R${preco:.2f}')
elif instalacao == 'I':
    preco = mult(kwh, classificacao_energia['I'][0]) if kwh <= 5000 else mult(kwh, classificacao_energia['I'][1])
    print(f'Preço: R${preco:.2f}')
else:
    print('Tipo de instalação inexistente!')
