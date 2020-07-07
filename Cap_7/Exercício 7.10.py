'''
Ex 7.10:
    Jogo da velha
'''
# Função criadas
from funs import cor
from funs import mat1
from funs import empate

lista = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
y = 1
# Primeira Matriz com as marcações
for i, l in enumerate(lista):
    if lista[i] == 0:
        y = 1
    elif lista[i] == 1:
        y = 4
    if lista[i] == 2:
        y = 7
    for c in l:
        print(f'| {y} ', end='| ')
        y += 1
    print()
while True:

         # Jogador 1
        while True:
            j1 = int(input(f'Jogador 1, onde quer colocar o {cor("X", 5)}: '))
            if j1 == 1:
                if lista[0][0] == '-':
                    lista[0][0] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 2:
                if lista[0][1] == '-':
                    lista[0][1] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 3:
                if lista[0][2] == '-':
                    lista[0][2] = cor('X', 5)
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 4:
                if lista[1][0] == '-':
                    lista[1][0] = cor(cor('X', 5), 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 5:
                if lista[1][1] == '-':
                    lista[1][1] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 6:
                if lista[1][2] == '-':
                    lista[1][2] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 7:
                if lista[2][0] == '-':
                    lista[2][0] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 8:
                if lista[2][1] == '-':
                    lista[2][1] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j1 == 9:
                if lista[2][2] == '-':
                    lista[2][2] = cor('X', 5)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            else:
                print(cor('Erro! Digite 1,2,3,4,5,6,7,8 ou 9.', 2))

        # Matriz na tela
        mat1(lista)

        # Verificação da matriz para ganhar o jogo ou empatá-lo
        # Primeira linha igual
        if lista[0][0] == 'X' and lista[0][1] == 'X' and lista[0][2] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break
        # Segunda linha igual:
        elif lista[1][0] == 'X' and lista[1][1] == 'X' and lista[1][2] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break
        # Terceira linha igual:
        elif lista[2][0] == 'X' and lista[2][1] == 'X' and lista[2][2] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break
        # Primeira coluna igual
        elif lista[0][0] == 'X' and lista[1][0] == 'X' and lista[2][0] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break

        # Segundaa coluna igual
        elif lista[0][1] == 'X' and lista[1][1] == 'X' and lista[2][1] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break

        # Terceira coluna igual
        elif lista[0][2] == 'X' and lista[1][2] == 'X' and lista[2][2] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break

        # Diagona principal
        elif lista[0][0] == 'X' and lista[1][1] == 'X' and lista[2][2] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break

        # Diagona secundária
        elif lista[0][2] == 'X' and lista[1][1] == 'X' and lista[2][0] == 'X':
            print(cor('O jogador 1 venceu!', 4))
            break
        # Empate
        elif empate(lista):
            print(cor('EMPATE!', 4))
            break
    # ------------------------------------------------------------------------

        # Jogador 2
        while True:
            j2 = int(input(f'Jodador 2, onde quer colocar o {cor("O", 1)}: '))
            if j2 == 1:
                if lista[0][0] == '-':
                    lista[0][0] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 2:
                if lista[0][1] == '-':
                    lista[0][1] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 3:
                if lista[0][2] == '-':
                    lista[0][2] = cor('O', 1)
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 4:
                if lista[1][0] == '-':
                    lista[1][0] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 5:
                if lista[1][1] == '-':
                    lista[1][1] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 6:
                if lista[1][2] == '-':
                    lista[1][2] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 7:
                if lista[2][0] == '-':
                    lista[2][0] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 8:
                if lista[2][1] == '-':
                    lista[2][1] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            elif j2 == 9:
                if lista[2][2] == '-':
                    lista[2][2] = cor('O', 1)
                    break
                else:
                    print(cor('Posição já ocupada!', 1))
            else:
                print(cor('Erro! Digite 1,2,3,4,5,6,7,8 ou 9.', 2))

        # Matriz na tela
        mat1(lista)

        # Verificação da matriz para ganhar o jogo ou empatá-lo:
        # Primeira linha igual
        if lista[0][0] == 'O' and lista[0][1] == 'O' and lista[0][2] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break

        # Segunda linha igual:
        elif lista[1][0] == 'O' and lista[1][1] == 'O' and lista[1][2] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break

        # Terceira linha igual:
        elif lista[2][0] == 'O' and lista[2][1] == 'O' and lista[2][2] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break

        # Primeira coluna igual
        elif lista[0][0] == 'O' and lista[1][0] == 'O' and lista[2][0] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break

        # Segundaa coluna igual
        elif lista[0][1] == 'O' and lista[1][1] == 'O' and lista[2][1] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break
        # Terceira coluna igual
        elif lista[0][2] == 'O' and lista[1][2] == 'O' and lista[2][2] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break

        # Diagona principal
        elif lista[0][0] == 'O' and lista[1][1] == 'O' and lista[2][2] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break
        # Diagona secundária
        elif lista[0][2] == 'O' and lista[1][1] == 'O' and lista[2][0] == 'O':
            print(cor('O jogador 2 venceu!', 4))
            break
        # Empate
        elif empate(lista):
            print(cor('EMPATE!', 4))
            break
