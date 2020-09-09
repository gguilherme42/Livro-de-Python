import agenda25

agenda25.le('Agenda.txt')
while True:
    opcao = agenda25.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda25.novo()
    elif opcao == 2:
        agenda25.altera()
    elif opcao == 3:
        agenda25.apaga()
    elif opcao == 4:
        agenda25.lista()
    elif opcao == 5:
        agenda25.grava()
    elif opcao == 6:
        agenda25.le()
    elif opcao == 7:
        agenda25.ordena()
    else:
        print('Opção inválida! Digite novamente.')
