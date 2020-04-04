'''
Ex 6.17:
    Altere o programa da listagem 6.53 de forma a solicitar
    ao usuário o produto e quantidade vendida. Verifique se o nome
    do produto digitado existe no dicionário, e só então efetue a baixa
    em estoque.
'''

Estoque = {'tomate': [1000, 2.3],
           'alface': [500, 0.45],
           'batata': [2001, 1.2],
           'feijão': [100, 1.5]}
venda = []
itens = []
tot = 0
print('=' * 30)
while True:
    # Estoque
    print('-' * 30)
    for k, v in Estoque.items():
        print(f'- Descrição: {k}')
        print(f'  Quantidade {v[0]}')
        print(f'  Preço: {v[1]}')
    print('-' * 30)

    # Validação do produto do estoque
    while True:
        p = str(input('Produto: ')).strip().lower()
        if p in Estoque:
            break
        else:
            print('Produto fora de estoque! Digite um produto do estoque.')

    # Validação da quantidade do estoque
    while True:
        q = int(input('Quantidade: '))
        if q > Estoque[p][0]:
            print('Quantidade superior a do estoque. Digite uma quantidade inferior.')
        else:
            break

    # Adição do produto e quantidade
    itens.append(p)
    itens.append(q)
    venda.append(itens[:])
    itens.clear()

    # Validação da pergunta de continuação
    while True:
        per = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if per in 'SN':
            break
        else:
            print('Respota inválida! Digite S ou N')
    if per == 'N':
        break
print('=' * 30)

# Operação de venda
print('Nota: ')
for op in venda:
    produto, quantidade = op
    preco = Estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto}: {quantidade} x {preco:.2f} = {custo:.2f}')
    # Baixa do estoque
    Estoque[produto][0] -= quantidade
    # Gasto total
    tot += custo
print(f'Gasto total: {tot:.2f}')
print('-' * 30)
print(f'Estoque: ')
for k, v in Estoque.items():
    print(f'- Descrição: {k}')
    print(f'  Quantidade {v[0]}')
    print(f'  Preço: {v[1]}')
print('-' * 30)
