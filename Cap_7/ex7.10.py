
matriz = {'A': {1: '-', 2: '-', 3: '-'},
          'B': {1: '-', 2: '-', 3: '-'},
          'C': {1: '-', 2: '-', 3: '-'}}


def mostraVelha():
    global  matriz
    print(f'      1     2     3   ')
    for i, e in matriz.items():
        print(f'{i}   | {e[1]} | | {e[2]} | | {e[3]} | ')


def jogador_entrada(numerojogador=1):
    simbolo = 'X' if numerojogador == 1 else 'O'
    while True:
        try:
            jogador_entrada = input(f'Digite a posição do {simbolo} (letra + número): ').strip().upper()[:2]
            try:
                if int(jogador_entrada[1]) and (jogador_entrada[0] == 'A' or
                jogador_entrada[0] == 'B' or jogador_entrada[0] == 'C'):
                    return jogador_entrada
            except:
                print('Posição inválida! Digite uma posição válida.')
        except:
            print('Posição inválida! Digite uma posição válida.')


mostraVelha()
while True:

    jog1 = jogador_entrada(1)
    jog2 = jogador_entrada(2)

    try:
        matriz[jog1[0]][int(jog1[1])] = 'X'
        matriz[jog2[0]][int(jog2[1])] = 'O'
    except:
        print('Digite uma posição válida')
    else:
        mostraVelha()
