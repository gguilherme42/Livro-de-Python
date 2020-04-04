'''
Ex 6.8:
    Modifique o exemplo para pesquisar dois valores. Na impressão,
    indique qual foi encontrado primeiro.
'''
l = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
p1 = int(input('Digite outro valor a procurar: '))
while True:
    x = - 1
    y = - 1
    for i, v in enumerate(l):
        if l[i] == p:
            x = i
        elif l[i] == p1:
            y = i
    if x < 0 and y < 0:
        print(f'Valor {p} e {p1} não encontrados!')
        break
    else:
        if not(x < 0) and not(y < 0):
            #  Se Y for menor que X, isto é, o índice de um for menor que o outros. Então.
            # Y foi encontrado primeiro.
            if y < x:
                print(f'Achou {p} na posição {x}')
                print(f'Achou {p1} na posição {y}')
                print(f'{p1} foi encontrado primeiro.')
                break
            else:
                print(f'Achou {p} na posição {x}')
                print(f'Achou {p1} na posição {y}')
                print(f'{p} foi encontrado primeiro.')
                break
        elif y < 0:
            print(f'Achou {p} na posição {x}')
            print(f'{p1} não foi encontraddo!')
            break
        else:
            print(f'{p} não foi encontraddo!')
            print(f'Achou {p1} na posição {y}')
            break
