DicioErros = {0: '''X==:==
X  :  
X    
X
X
X
X-------''',
              1: '''X==:==
X  :  
X  O  
X
X
X
X-------''',
              2: '''X==:==
X  :  
X  O  
X  |
X
X
X-------''',
              3: '''X==:==
X  :  
X  O  
X \|
X
X
X-------''',
              4: '''X==:==
X  :  
X  O  
X \|/
X
X
X-------''',
              5: '''X==:==
X  :  
X  O  
X \|/
X |
X
X-------''',
              6: '''X==:==
X  :  
X  O  
X \|/
X | |
X
X-------'''}

palavras = ['amor', 'fato', 'mito', 'puta', 'esmo', 'brio', 'caos', 'vide', 'não',
            'auge', 'sede', 'céu', 'ermo', 'pois', 'mote', 'apto', 'como', 'crer', 'suma',
            'tolo', 'vão', 'vida', 'cota', 'saga', 'veio', 'medo', 'ruim', 'urge', 'réu',
            'zelo', 'ente', 'mãe', 'pude', 'idem', 'soar', 'coxo', 'ater', 'gozo', 'fase',
            'rima', 'casa', 'cedo', 'voga', 'cujo', 'rude', 'sina', 'sela', 'onde', 'cela', 'nojo',
            'face', 'meio', 'teor', 'mais', 'tudo', 'pose', 'auto', 'teve', 'asco', 'base', 'ante',
            'alvo', 'alva', 'numa', 'agir', 'traz']

while True:
    numero = int(input('Digite um número: '))
    i = (numero * 776) % len(palavras)
    try:
        palavra = palavras[i]
    except:
        print('Índice inexistente. Digite outro número.')
    else:
        break

for x in range(100):
    print()


digitadas = []
acertos = []
erros = 0
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

    # Boneco
    try:
        print(DicioErros[erros])
    except:
        print('Erro!')
    else:
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra secreta era: {palavra}')
            break


digitadas = []
acertos = []
erros = 0
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

    # Boneco
    try:
        print(DicioErros[erros])
    except:
        print('Erro!')
    else:
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra secreta era: {palavra}')
            break

