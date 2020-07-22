lista = list(range(5))
p1 = int(input('Valor 1: '))
p2 = int(input('Valor 2: '))
posicao = [[], []]
x = 0
while x < len(lista):
    if lista[x] == p1:
        if posicao[1]:
            posicao[0].append(x)
            break
        else:
            posicao[0].append(x)
    elif lista[x] == p2:
        if posicao[0]:
            posicao[1].append(x)
            break
        else:
            posicao[1].append(x)
    x += 1

if not posicao[0] and not posicao[1]:
    print('Valores não encontrados!')
elif not posicao[0] and posicao[1]:
    print('Valor 1 não encontrado!')
    print(f'Valor 2 encontrado na posição: {posicao[1][0]}')
elif posicao[0] and not posicao[1]:
    print(f'Valor 1 encontrado na posição: {posicao[0][0]}')
    print('Valor 2 não encontrado!')
else:
    if p1 == p2:
        print(f'Valores encontrados na posição: {posicao[0][0]}')
    elif posicao[0][0] < posicao[1][0]:
        print(f'Valor 1 econtrado pirmeiro, posição: {posicao[0][0]}')
        print(f'Valor 2 encontrado na posição: {posicao[1][0]}')
    elif posicao[0][0] > posicao[1][0]:
        print(f'Valor 2 econtrado pirmeiro, posição: {posicao[1][0]}')
        print(f'Valor 1 encontrado na posição: {posicao[0][0]}')
