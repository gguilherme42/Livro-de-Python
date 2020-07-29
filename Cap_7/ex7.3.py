s1 = list(input('String 1: ').upper())
s2 = list(input('String 2: ').upper())
lista = []
for l in s2:
    if l not in s1:
        lista.append(l)


for l in s1:
    if l not in s2:
        lista.append(l)

print(lista)
