# Minha resolução ficou um pouco diferente do que como exercício pedia para fazer, no entanto,
# fiz o que exercício pedia.


def dadosfila(fila):
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Filha atual {fila}')
    print('''Digite: 
    F - para adicionar um cliente no fim da fila
    A - para realizar o atendimento
    S - para sair''')


def operacaofila(op, fila, ultimo):
    for l in op:
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
            return True
        else:
            print(f'Operação {l} inválida!')
    return False


filaA = list(range(1, 11))
filaB = list(range(1, 200))
ultimoA = len(filaA) - 1
ultimoB = len(filaB) - 1

while True:
    print(f'Fila A: {filaA}\nFila B: {filaB}')
    escolha = input('Qual fila deseja trabalhar A ou B?(Digite A, B ou S para sair) ').strip().upper()[0]
    if escolha == 'S':
        break
    if escolha != 'S' and escolha != 'A' and escolha != 'B':
        print('Opção inválida! Digte A, B ou S.')
    else:
        fila = filaA if escolha == 'A' else filaB
        ultimo = ultimoA if escolha == 'A' else ultimoB
        dadosfila(fila)
        operacao = input('Operação (F, A ou S): ').strip().upper()
        if operacao == 'S':
            break
        saida = operacaofila(operacao, fila, ultimo)
        if saida:
            break
