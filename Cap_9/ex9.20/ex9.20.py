import agenda21

while True:
    opcao = agenda21.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda21.novo()
    elif opcao == 2:
        agenda21.altera()
    elif opcao == 3:
        agenda21.apaga()
    elif opcao == 4:
        agenda21.lista()
    elif opcao == 5:
        agenda21.grava()
    elif opcao == 6:
        agenda21.le()
    elif opcao == 7:
        agenda21.ordena()
    else:
        print('Opção inválida! Digite novamente.')
