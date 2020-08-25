n = int(input('Quantidade de arquivos: '))
listaDeArquivos = [input('Nome do arquivo: ').strip() for i in range(n)]
for i in listaDeArquivos:
    arq = open(i, 'r')
    for linha in arq.readlines():
        print(linha)
    arq.close()
