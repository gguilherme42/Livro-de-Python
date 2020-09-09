import agenda27

agenda27.le('Agenda.txt')
while True:
    opcao = agenda27.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda27.novo()
    elif opcao == 2:
        agenda27.altera()
    elif opcao == 3:
        agenda27.apaga()
    elif opcao == 4:
        agenda27.lista()
    elif opcao == 5:
        agenda27.grava()
    elif opcao == 6:
        agenda27.le()
    elif opcao == 7:
        agenda27.ordena()
    else:
        print('Opção inválida! Digite novamente.')
