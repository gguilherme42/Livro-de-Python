'''
Ex 6.16:
    Modifique o programa da listagem 6.44 para ordenar a lista
    em ordem decrescente. L = [1, 2, 3, 4, 5] deve ser ordenada como
    L = [5, 4, 3, 2, 1].
'''
L = [1, 4, 5, 3, 2]
comp = len(L)
while comp > 1:
    trocou = False
    i = 0
    while i < comp - 1:
        if L[i] != (comp - 1):
            trocou = True
            if L[i] < L[(i + 1)]:
                t = L[i]
                L[i] = L[(i + 1)]
                L[(i + 1)] = t
        i += 1
    if not trocou:
        break
    comp -= 1

for c in L:
    print(c)
