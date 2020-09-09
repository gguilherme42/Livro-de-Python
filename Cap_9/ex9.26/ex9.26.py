import agenda26

agenda26.le('Agenda.txt')
while True:
    opcao = agenda26.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda26.novo()
    elif opcao == 2:
        agenda26.altera()
    elif opcao == 3:
        agenda26.apaga()
    elif opcao == 4:
        agenda26.lista()
    elif opcao == 5:
        agenda26.grava()
    elif opcao == 6:
        agenda26.le()
    elif opcao == 7:
        agenda26.ordena()
    else:
        print('Opção inválida! Digite novamente.')
