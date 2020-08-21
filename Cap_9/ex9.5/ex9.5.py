arquivo = open('par.txt', 'r')
pares = [i[:-1] for i in arquivo.readlines()] #remove o último caractere = \n
arquivo.close()
arquivo = open('parInvertido.txt', 'w')
for i in sorted(pares, reverse=True):
     arquivo.write(f'{i}\n')
     print(i)
arquivo.close()

