'''
Ex 6.4:
    O que acontece quanto não verificamos se a lista está vazia
    antes de chamarmos o método pop?
    # Resultado: -> IndexError: pop from empty list

Ex 6.5:
    Altere o program de listagem 6.21 de forma a poder
    trabalhar com vários comandos digitados de uma só vez.
    Atualmente, apenas um comando pode ser inserido por vez.
    Altere-o de forma a considerar operação como uma string.
    Exemplo: FFFAAAS significaria três chegadas de novos clientes,
    três atendimentos e, finalmente, a saída do programa.
'''
from time import sleep
último = 10
fila = list(range(0, último+1))
while True:
    print('='*30)
    print(f'Total de clientes na fila: {len(fila)}', end='\n')
    print(f'Fila atual: \n{fila}', end='\n')
    print(f'Digite F para adicionar um cliente, ou A para atender.')
    print('Digite S para sair.')
    op = str(input('Operação (F, A ou S): ')).strip().upper()
    for c in op: # Percorrendo a string
        if c == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido ')
            else:
                print('Fila vazia! Ninguém para antender.')
        elif c == 'F':
             último += 1 # Incremente o índice (ticket) do novo cliente
             print(f'Cliente {último} adicionado na fila.')
             fila.append(último)
        elif c == 'S':
            print('Saindo...')
            sleep(0.5)
            break
        else:
            print('Operação inválida! Digite: F, A ou S.')
    print('='*30)
    if 'S' in op:
        break
