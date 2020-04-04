'''
Ex 6.8:
    Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
    a mesma tarefa, mas sem utilizar a variável achou. Dica: Observe
    a condição de saída do while.
'''

l = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
while True:
    x = - 1
    for i, v in enumerate(l):
        if l[i] == p:
            x = i
    if x < 0:
        print(f'Valor {p} não encontrado!')
        break
    else:
        print(f'Achou {p} na posição {x}')
        break
