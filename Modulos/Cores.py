def colorir(frase, cor, b=0):
    '''
    Colore uma string
    :param frase: frase para colorir
    :param cor: nome da cor no dicionário
    :param b: 0 para normal e 1 para negrito
    :return: string colorida
    '''
    cores = {'w': ['\033[0;30m', '\033[1;30m'],
             'r': ['\033[0;31m', '\033[1;31m'],
             'b': ['\033[0;34m', '\033[1;34m'],
             'g': ['\033[0;32m', '\033[1;32m'],
             'y': ['\033[0;33m', '\033[1;33m'],
             'c': ['\033[0;36m', '\033[1;36m'],
             'm': ['\033[0;35m', '\033[1;35m'],
             'gr': ['\033[0;37m', '\033[1;37m'],
             'n': '\033[m'}
    try:
        return f'{cores[cor][b]}{frase}{cores["n"]}'
    except KeyError:
        print(f'{cores["r"][1]}Cor inválida!{cores["n"]}')


print(f'{colorir("ATENÇÃO!", "w", 1)}')
