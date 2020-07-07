'''
Exercício 8.15:
    Utilizando a função type, escreva uma função recursiva que imprima
    os elementos de uma lista. Considere o caso de listas dentro de listas,
    como L = [1, [2, 3, 4, [5, 6, 7]]]. A cada nível, imprima a lista
    mais à direita, como fazemos ao identar blocos em python. Dica:
    envie o nível atual como parâmetro e utilize-o para calcular a
    quantidade de espaços em branco de espaços em branco à esquerda de cada
    elemento.
'''


def exerc(*l):
    for x in l:
        if not(type(x) == list):
            print(x)
        else:
            for z in x:
                if not(type(z) == list):
                    print(z)
                else:
                    return exerc(z)


L = [1, [2, 3, 4, [5, 6, [7, 8, 9, 10]]]]

exerc(L)
