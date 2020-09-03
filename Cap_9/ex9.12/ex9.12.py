palavras = {}
arquivo = open('entrada.txt', 'r')
c = 0
for p in arquivo.readlines():
    lista = p.split(' ')
    for l in lista:
        if '\n' not in l:
            c += 1
        else:
            c = 1
        try:
            palavras[l][0] += 1
        except:
            palavras[l] = [1, c]

arquivo.close()
print(palavras)
