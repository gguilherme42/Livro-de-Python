estoque = {"tomate": [1000, 2.3],
           "feijao": [500, 1.5],
           "batata": [600, 1.2],
           "alface": [900, 0.5]}
total = 0


def em_estoque():
    global estoque
    print('\nEstoque:')
    for chave, dados in estoque.items():
        print(f'→ Produto: {chave} | Quant.: {dados[0]:5} | Preço: R${dados[1]:4}')
    print("")


def comprado(prod, q, prec, c):
    print(f'''Nota:
* Produto: {prod}
* Quantidade: {q}
* Preço unitário: R${prec:.2f}
* Custo: R${custo:.2f}''')


def valida_prod():
    global estoque
    while True:
        try:
            p = input('Produto: ').strip().lower()
            if estoque[p]:
                return p
        except:
            print('Digite um produto válido!')


def valida_quant(p):
    global estoque
    while True:
        q = int(input('Quantidade: '))
        if 1 <= q <= estoque[p][0]:
            return q
        else:
            print('Quantidade inválida ou fora de estoque.')


for i in range(5):
    em_estoque()
    produto = valida_prod()
    quantidade = valida_quant(produto)
    preco = estoque[produto][1]
    custo = preco * quantidade
    comprado(produto, quantidade, preco, custo)
    estoque[produto][0] -= quantidade
    total += custo

print(f'Gasto total: R${total:.2f}')

