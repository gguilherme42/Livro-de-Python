tabela = {'1': 0.5,
          '2': 1,
          '3': 4,
          '5': 7,
          '9': 8}

def caixaprint(dicio):
    print(f' Código |{"Preço":5}')
    for i, t in dicio.items():
        print(f'> {i:>2} {"-":>4} {t:3<}')


totc = 0
while True:
    caixaprint(tabela)
    codigo = input('Digite o código do produto: ').strip()
    if codigo == '0':
        break
    elif len(codigo) > 1:
        print('Valor inválido!')
        continue
    q = int(input('Digite a quantidade comprada: '))
    if codigo == '1':
        preco = tabela[codigo] * q
        totc += 1
    elif codigo == '2':
        preco = tabela[codigo] * q
        totc += 1
    elif codigo == '3':
        preco = tabela[codigo] * q
        totc += 1
    elif codigo == '5':
        preco = tabela[codigo] * q
        totc += 1
    elif codigo == '9':
        preco = tabela[codigo] * q
        totc += 1
    else:
        print('Código inválido!')

print(f'Total de compras: {totc}')
