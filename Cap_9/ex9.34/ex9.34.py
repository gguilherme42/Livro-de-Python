from Modulos import Cores
import random, time

# Máximo uma hora.
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

inicio = time.localtime().tm_min
arquivo = open('palavras.txt', 'r')
escolhido = [line[:-1] for line in arquivo.readlines()]
arquivo.close()
palavra = random.choice(escolhido)
digitadas = []
acertos = []
erros = 0
enforcado = ''
NomeJogador = input('Nome do jogador(a): ').strip().lower()
while True:
    senha = ''

    # Vai imprimir a senha que é a palavra a se descobrir
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)

    if senha == palavra:
        enforcado = 'NÃO'
        print(Cores.colorir('Você acertou!', 'y', 1))
        break

    tentativa = str(input('Digite um letra: ')).lower().strip()[0]

    if tentativa in digitadas:
        print(Cores.colorir('Você já digitou esta letra!', 'w', 1))
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
            print(Cores.colorir('Você errou!', 'w', 1))

    # Boneco
    try:
        print(DicioErros[erros])
    except:
        print(Cores.colorir('Erro!', 'r', 1))
    else:
        if erros == 6:
            enforcado = 'SIM'
            print(Cores.colorir('Enforcado!', 'r', 1))
            print(f'A palavra secreta era: {Cores.colorir(palavra,"w", 1)}')
            break

tempo_min = time.localtime().tm_min - inicio
arquivoArcade = open('jogos.txt', 'w')
arquivoArcade.write(f'Jogador(a): {NomeJogador} | Acertos: {len(acertos)} | '
                    f'erros: {erros} | Enforcado: {enforcado}'
                    f'Tempo do jogo: {tempo_min}:{time.localtime().tm_sec:02}')
arquivoArcade.close()
print(f'Tempo do jogo: {tempo_min}:{time.localtime().tm_sec:02}')
