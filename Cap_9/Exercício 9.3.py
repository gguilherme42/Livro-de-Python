'''
Ex. 9.3:
    Crie um programa que leia os arquivos pares.txt e impares.txt e que crie
    um só arquivo pareseimpares.txt com todas as linhas dos outros arquivos,
    de forma a preservar a ordem numérica.
'''
# Criação dos arquivos pares.txt e impares.txt
pares = open('pares.txt', 'w')
impares = open('impares.txt', 'w')
for n in range(1, 51):
    if n % 2 == 0:
        pares.write(f'{n} ')
    else:
        impares.write(f'{n} ')
pares.close()
impares.close()

# Criaçã de pareseimpares.txt e leitura de pares.txt e impares.txt
pei = open('pareseimpares.txt', 'w')
pares = open('pares.txt', 'r')
impares = open('impares.txt', 'r')
for n in pares:
    pei.write(f'{n} ')
pei.write('\n')
pares.close()
for n in impares:
    pei.write(f'{n} ')
impares.close()
pei.close()
