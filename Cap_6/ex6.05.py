def dadosfila(fila):
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Filha atual {fila}')
    print('''Digite: 
    F - para adicionar um cliente no fim da fila
    A - para realizar o atendimento
    S - para sair''')


fila = list(range(1, 11))
ultimo = len(fila) - 1
while True:
    saida = False
    dadosfila(fila)
    operacao = input('Operação (F, A ou S): ').strip().upper()
    if operacao == 'S':
        break
    else:
        for l in operacao:
            if l == 'F':
                ultimo += 1
                fila.append(ultimo)
            elif l == 'A':
                if fila:
                    atendido = fila.pop(0)
                    print(f'Cliente {atendido} atendido')
                else:
                    print('Fila vazia!')
            elif l == 'S':
                saida = True
                break
            else:
                print(f'Operação {l} inválida!')
    if saida:
        break