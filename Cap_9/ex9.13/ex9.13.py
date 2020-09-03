import sys
arquivo = open(sys.argv[1], 'r')
inicio = int(sys.argv[2])
fim = int(sys.argv[3])
for i in range(inicio, fim):
    print(arquivo.readline())
arquivo.close()
