'''
Exercício 9.16 até o 9.28:
    Controle de uma agenda de telefones.
'''
import fagenda
while True:
    op = fagenda.menu()
    if op == 0:
        fagenda.escreve('0 - SAINDO')
        break
    elif op == 1:
        fagenda.escreve('1 - NOVO CONTATO')
        fagenda.novo()
    elif op == 2:
        fagenda.escreve('2 - ALTERAÇÂO')
        fagenda.altera()
    elif op == 3:
        fagenda.escreve('3 - EXCLUSÃO')
        fagenda.apaga()
    elif op == 4:
        fagenda.escreve('4 - LISTA')
        fagenda.lista()
    elif op == 5:
        fagenda.escreve('5 - LISTA ORDENADA')
        fagenda.lista(ord=True)
    elif op == 6:
        fagenda.escreve('6 - SALVANDO ARQUIVO')
        fagenda.grava()
    elif op == 7:
        fagenda.escreve('7 - LENDO ARQUIVO')
        fagenda.ler(fagenda.pedenomeArquivo())

