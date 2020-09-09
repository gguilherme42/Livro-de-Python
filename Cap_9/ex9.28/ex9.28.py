import agenda28

agenda28.le('Agenda.txt')
while True:
    opcao = agenda28.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda28.novo()
    elif opcao == 2:
        agenda28.altera()
    elif opcao == 3:
        agenda28.apaga()
    elif opcao == 4:
        agenda28.lista()
    elif opcao == 5:
        agenda28.grava()
    elif opcao == 6:
        agenda28.le()
    elif opcao == 7:
        agenda28.ordena()
    else:
        print('Opção inválida! Digite novamente.')
