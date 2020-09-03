nome = input('nome do arquivo: ')
arquivo = open(nome, 'r', encoding='UTF-8')
arquivo_saida = open('arquivo_saida', 'w', encoding='UTF-8')
branco = 0
for linha in arquivo:
    linha = linha.rstrip()
    linha = linha.replace(' ', '')
    if linha == '':
        branco += 1
    else:
        branco = 0
    if branco < 2:
        arquivo_saida.write(linha)

arquivo_saida.close()
arquivo.close()
