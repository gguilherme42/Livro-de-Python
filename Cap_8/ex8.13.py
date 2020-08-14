def acertou(tentativa):
    from random import randint
    return True if tentativa == randint(1, 10) else False


acertos = erros = 0
while True:
    print(f' - Erros: {erros}\n - Acertos: {acertos}')
    if acertos == 3 or erros == 3:
        break
    n = int(input('Escolha um número entre 1 e 10: '))
    resp = acertou(n)
    print('Você acertou!' if resp else 'Você errou!' )
    if resp:
        acertos += 1
    else:
        erros += 1