s1 = list(input('String 1: ').upper())
s2 = list(input('String 2: ').upper())
lista = []
s3 = ""
for l in s1:
    for l2 in s2:
        if l == l2 and l not in lista:
            lista.append(l)

print(lista)
