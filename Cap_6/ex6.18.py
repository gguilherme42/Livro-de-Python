Qletras = {}
frase = input('Digite uma frase: ').strip()
for letra in frase:
    if letra != "":
        if letra not in Qletras:
            Qletras[letra] = 1
        else:
            Qletras[letra] += 1

print(Qletras)
