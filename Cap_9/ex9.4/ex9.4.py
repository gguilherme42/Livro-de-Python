import sys
if len(sys.argv) != 3:
    print('Uso: arquivo.py  "file1.txt" "file2.txt"')
else:
    arquivo1 = open(f'{sys.argv[1]}', 'r')
    primeiro = [i for i in arquivo1.readlines()]
    arquivo1.close()

    arquivo2 = open(f'{sys.argv[2]}', 'r')
    segundo = [i for i in arquivo2.readlines()]
    arquivo2.close()

    terceiro = primeiro + segundo
    arquivo_resultado = open('resultado.txt', 'w')
    for i in terceiro:
        print(i)
        arquivo_resultado.write(f'{i}')
    arquivo_resultado.close()
