#Igual ao 7.7
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

palavra = str(input('Digite a palavra secreta: ')).strip().lower()
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

