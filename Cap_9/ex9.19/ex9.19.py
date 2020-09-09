import agenda19

while True:
    opcao = agenda19.menu()
    if opcao == 0:
        break
    elif opcao == 1:
        agenda19.novo()
    elif opcao == 2:
        agenda19.altera()
    elif opcao == 3:
        agenda19.apaga()
    elif opcao == 4:
        agenda19.lista()
    elif opcao == 5:
        agenda19.grava()
    elif opcao == 6:
        agenda19.le()
