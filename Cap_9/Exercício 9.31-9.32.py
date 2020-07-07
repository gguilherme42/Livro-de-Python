'''
Ex. 9.31 - 9.32:
    Crie um programa que corrija o da listagem 9.20 de forma a verificar
    se z existe e é um diretório.
'''
import os
# Arquivo -> open('z', 'w').close()
# Diretório -> os.mkdir('z')
if os.path.exists('z'):
    if os.path.isdir('z'):
        print('\"z\" é um diretório.')
    elif os.path.isfile('z'):
        print('\"z\" é um arquivo.')
    else:
        print('\"z\" não é um diretório e não é um arquivo.')
else:
    print('\n\"z\" não existe.')


