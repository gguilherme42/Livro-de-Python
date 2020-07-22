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
    print('Valor 2 encontrado!')
elif posicao[0] and not posicao[1]:
    print('Valor 1 encontrado!')
    print('Valor 2 não encontrado!')
else:
    if p1 == p2:
        print('Valores encontrados!')
    elif posicao[0][0] < posicao[1][0]:
        print('Valor 1 econtrado pirmeiro!')
        print('Valor 2 encontrado!')
    elif posicao[0][0] > posicao[1][0]:
        print('Valor 2 econtrado pirmeiro!')
        print('Valor 1 encontrado!')
