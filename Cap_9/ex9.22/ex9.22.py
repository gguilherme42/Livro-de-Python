import agenda22

while True:
    opcao = agenda22.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda22.novo()
    elif opcao == 2:
        agenda22.altera()
    elif opcao == 3:
        agenda22.apaga()
    elif opcao == 4:
        agenda22.lista()
    elif opcao == 5:
        agenda22.grava()
    elif opcao == 6:
        agenda22.le()
    elif opcao == 7:
        agenda22.ordena()
    else:
        print('Opção inválida! Digite novamente.')
