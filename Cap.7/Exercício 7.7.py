'''
Ex 7.7:
    Modifique o programa de forma a escrever a palavra secreta
    caso o jogador perca.
'''
palavra = str(input('Digite a palavra secreta: ')).strip().lower()
# Pulando várias linhas para que o jogador não veja a palavra secreta
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
# Linha2 -> Torso do boneco; Linha3 -> Dorso do boneco
linha2 = linha3 = ''
while True:
    senha = ''

    # Vai imprimir a senha que é a palavra a se descobrir
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)

    if senha == palavra:
        print('Você acertou!')
        break

    tentativa = str(input('Digite um letra: ')).lower().strip()[0]

    if tentativa in digitadas:
        print('Você já digitou esta letra!')
        # O continue toca novamente para o loop
        continue
    else:

        # Tentantiva dentro do que foi digitado
        digitadas += tentativa

        # Tentativa dentro dos acertos
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')

    # Início da corda
    print('X==:==\nX  :  ')
    # Cabeça
    print('X  O  ' if erros >= 1 else 'X')
    if erros == 2:
        linha2 = ' |'
    elif erros == 3:
        linha2 = '\|'
    elif erros == 4:
        linha2 = '\|/'

    if erros == 5:
        linha3 = ' /  '
    elif erros >= 6:
        linha3 = ' / \ '

    print(f'X {linha2}')
    print(f'X{linha3}')
    # Chão:
    print('X\n=============')
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra secreta era: {palavra}')
        break
