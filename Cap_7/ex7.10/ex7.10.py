matriz = {'A': {"1": '-', "2": '-', "3": '-'},
          'B': {"1": '-', "2": '-', "3": '-'},
          'C': {"1": '-', "2": '-', "3": '-'}}


def empate_vitoria(nome_jogador, lista_de_posicoes):
    comprimento = len(lista_de_posicoes[0]) + len(lista_de_posicoes[1])
    if comprimento >= 6:
        if comprimento == 10:
            print('Empate!')
            return True
        linha = set(lista_de_posicoes[1])
        print(f'linha: {linha}')
        col = set(lista_de_posicoes[0])
        print(f'Coluna: {col}')
        resultado = len(col) + len(linha)
        if resultado == 4 or resultado == 6:
            print(f'Vitória! Jogador(a) {nome_jogador} venceu!')
            return True
    return None


def letra_para_numero(letra):
    if letra == 'A':
        return 1
    elif letra == 'B':
        return 2
    elif letra == 'C':
        return 3


def mostraVelha():
    global matriz
    print('TABELA:')
    print(f'      1     2     3   ')
    for i, e in matriz.items():
        print(f'{i}   | {e["1"]} | | {e["2"]} | | {e["3"]} | ')


def posicaoOcupada(entrada):
    global matriz
    return True if matriz[entrada[0]][entrada[1]] != '-' else False


def validaEntrada(entrada):
    return True if (entrada[0] in 'ABC') and (entrada[1] in '123') else False


def jogador_entrada(simbolo):
    while True:
        try:
            entrada = input(f'Digite a posição do {simbolo} (letra + número): ').strip().upper()[:2]
        except:
            print('Posição inválida! Digite uma posição válida.')
        else:
            if not validaEntrada(entrada):
                print('Posição inválida! Digite uma posição válida.')
                continue
            if posicaoOcupada(entrada):
                print('Posição já ocupada! Digite uma posição não ocupada.')
                continue
            return entrada


if __name__ == '__main__':
    userX = (input('Nome do jogador(a) 1: ').strip().capitalize(), input('Simbolo (X ou O): ').strip().upper()[0], [[], []])
    userO = (input('Nome do jogador(a) 2: ').strip(), 'O' if userX[1] == 'X' else 'X', [[], []])

    mostraVelha()
    while True:

        jog1 = jogador_entrada(userX[1])
        userX[2][0].append(letra_para_numero(jog1[0]))
        userX[2][1].append(int(jog1[1]))

        matriz[jog1[0]][jog1[1]] = userX[1]

        mostraVelha()
        if empate_vitoria(userX[0], userX[2]):
            break

        jog2 = jogador_entrada(userO[1])
        userO[2][0].append(letra_para_numero(jog2[0]))
        userO[2][1].append(int(jog2[1]))


        matriz[jog2[0]][jog2[1]] = userO[1]

        mostraVelha()

        if empate_vitoria(userO[0], userO[2]):
            break

