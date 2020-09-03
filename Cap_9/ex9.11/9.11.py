palavras = {}
arquivo = open('words.txt', 'r')
for p in arquivo.readlines():
    palavra = p.split(' ')
    for l in palavra:
        try:
            palavras[l] += 1
        except:
            palavras[l] = 1
arquivo.close()
print(palavras)
