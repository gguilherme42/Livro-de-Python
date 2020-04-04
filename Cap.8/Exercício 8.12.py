'''
Ex. 8.12:
    Escreva uma função que receba uma string e uma lista. A função deve comparar
    a string passada com os elementos da lista, também passado como parâmetro. Retorne
    o valor verdadeiro se a string for encontrada dentro da lista, e falso em caso
    contrário.
'''


def comp(*l, msg=''):
    ig = False
    for i, v in enumerate(l):
        if type(l[i]) == str and v == msg:
            ig = True
    return ig


lista = ['a', 'b', 'c']

print(comp(lista, msg='b'))
