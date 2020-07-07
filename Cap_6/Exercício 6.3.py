'''
Ex 6.3:
    Faça um programa que percorra duas listas e gere uma
    terceira sem elementos repetidos.
'''
l = [1, 2, 3, 4, 5]
b = [1, 0, 4, 6, 5]
lista = []
for i, v in enumerate(l):
    if l[i] not in b:
        if l[i] not in lista:
            lista.append(l[i])
    for i, v in enumerate(b):
        if b[i] not in l:
            if b[i] not in lista:
                lista.append(b[i])

print(l)
print(b)
print(sorted(lista))
