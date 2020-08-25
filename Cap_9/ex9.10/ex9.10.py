n = int(input('Quantidade de arquivos: '))
listaDeArquivos = [input('Nome do arquivo: ').strip() for i in range(n)]
grande_arq = open('GrandeArquivo_Saida.txt', 'w')
for i in listaDeArquivos:
    arq = open(i, 'r')
    for linha in arq.readlines():
        grande_arq.write(linha)
    arq.close()
grande_arq.close()


