s1 = input('String: ').upper().strip()
letras = {}
for l in s1:
    try:
        letras[l] += 1
    except KeyError:
        letras[l] = 1
print(letras)
