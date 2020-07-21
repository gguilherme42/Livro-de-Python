
def menu():
    print("")
    print(f'''<------ MENU ------>
    A - para adição
    S - para subtração
    D - para divisão
    M - para múltiplicação
    X - para sair''')


def Aritmetica(a, operacao):
    arit = {'A': lambda a, b: a + b,
            'S': lambda a, b: a - b,
            'D': lambda a, b: a / b,
            'M': lambda a, b: a * b}

    if operacao == 'A':
        for i in range(1, 11):
            print(f'{a} + {i} = {arit[operacao](a, i)}')
    elif operacao == 'S':
        for i in range(1, 11):
            print(f'{a} - {i} = {arit[operacao](a, i)}')
    elif operacao == 'D':
        for i in range(1, 11):
            print(f'{a} / {i} = {arit[operacao](a, i)}')
    if operacao == 'M':
        for i in range(1, 11):
            print(f'{a} * {i} = {arit[operacao](a, i)}')


while True:
    a = int(input('Número: '))
    menu()
    while True:
        op = input('Operação: ').strip().upper()[0]
        if op == 'X':
            break
        elif op not in 'ASDM':
            print('Digite uma operação válida')
        else:
            Aritmetica(a, op)
    if op == 'X':
        break
