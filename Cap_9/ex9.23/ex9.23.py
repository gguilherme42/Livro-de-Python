import agenda23

agenda23.le('Agenda.txt')
while True:
    opcao = agenda23.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda23.novo()
    elif opcao == 2:
        agenda23.altera()
    elif opcao == 3:
        agenda23.apaga()
    elif opcao == 4:
        agenda23.lista()
    elif opcao == 5:
        agenda23.grava()
    elif opcao == 6:
        agenda23.le()
    elif opcao == 7:
        agenda23.ordena()
    else:
        print('Opção inválida! Digite novamente.')
