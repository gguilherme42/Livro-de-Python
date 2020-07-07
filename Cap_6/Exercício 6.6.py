'''
Ex 6.6:
    Modifique o programa para trabalhar com duas filas. Para facilitar
    seu trabalho, considere o comando A para atendimento da fila 1;
    e B para fila 2, para atendimento da fila 2. O mesmo para a chegada de
    clientes: F para fila 1; e G para fila 2.
'''
from time import sleep
ultimo1 = ultimo2 = 10
fila1 = list(range(0, ultimo1 + 1))
fila2 = list(range(0, ultimo2 + 1))
while True:
    print('='*30)
    print(f'Total de clientes na fila 1: {len(fila1)}')
    print(f'Total de clientes na fila 2: {len(fila2)}')
    print(f'Fila atual: \nfila 1: {fila1}\nfila 2: {fila2}')
    print(f'''Operações:
Adicionar clientes:
    -> F para fila 1; 
    -> G para fila 2.
Atender clientes:
    -> A para fila 1; 
    -> B para fila 2.
Sair:
    -> S.
    ''')
    op = str(input('Operação: ')).strip().upper()
    for c in op: # Percorrendo a string
        # Atendimento de clientes:
        # - Fila 1
        if c == 'A':
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)
                print(f'Cliente {atendido1} da fila 1, atendido ')
            else:
                print('Fila vazia! Ninguém para antender.')
        # - Fila 2
        elif c == 'B':
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)
                print(f'Cliente {atendido2} da fila 2, atendido ')
            else:
                print('Fila vazia! Ninguém para antender.')
        # Adição de clientes:
        # Fila 1
        elif c == 'F':
             ultimo1 += 1  # Incremente o índice (ticket) do novo cliente na fila 1
             print(f'Cliente {ultimo1} adicionado na fila 1.')
             fila1.append(ultimo1)
        # Fila 2
        elif c == 'G':
             ultimo2 += 1  # Incremente o índice (ticket) do novo cliente na fila 2
             print(f'Cliente {ultimo2} adicionado na fila 2.')
             fila2.append(ultimo2)
        # Saída
        elif c == 'S':
            print('Saindo...')
            sleep(0.5)
            break
        else:
            print('Operação inválida! Digite: F, A ou S.')
    print('='*30)
    # Saída
    if 'S' in op:
        break
print('-' * 30)
print(f'Total de clientes na fila 1: {len(fila1)}')
print(f'Total de clientes na fila 2: {len(fila2)}')
print(f'Fila atual: \nfila 1: {fila1}\nfila 2: {fila2}')
print('-' * 30)
