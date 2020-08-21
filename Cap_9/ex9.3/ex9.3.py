# impar = open('impar.txt', 'w')
# par = open('par.txt', 'w')
# for i in range(0, 3000):
#     if i % 2 == 0:
#         par.write(f'{i}\n')
#     else:
#         par.write(f'{i}\n')
# impar.close()
# par.close()

arquivo = open('par.txt', 'r')
par = [i for i in arquivo.readlines()]
arquivo.close()
arquivo = open('impar.txt', 'r')
impar = [i for i in arquivo.readlines()]
arquivo.close()
parEimpar = par + impar
arquivo = open('parEimpar.txt', 'w')
for i in parEimpar:
    arquivo.write(f'{i}')
arquivo.close()

