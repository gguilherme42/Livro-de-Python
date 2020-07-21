valor = float(input('Digite o valor a pagar: R$'))
a_pagar = round(valor, 2)
cedula = 100
moeda = 0.5
dinheiro = {'Cedulas': [],
            'Moedas': []}

while True:
    if 1 > a_pagar > 0:
        if moeda <= a_pagar:
            q = a_pagar // moeda
            a_pagar = round( a_pagar - q * moeda, 2)
            dinheiro['Moedas'].append([moeda, q])
        else:
            if a_pagar == 0:
                break
            if moeda == 0.5:
                moeda = 0.2
            elif moeda == 0.2:
                moeda = 0.1
            elif moeda == 0.1:
                moeda = 0.05
            elif moeda == 0.05:
                moeda = 0.01
    else:
        if cedula <= a_pagar:
            q = a_pagar // cedula
            a_pagar -= q * cedula
            dinheiro['Cedulas'].append([cedula, q])
        else:
            if a_pagar == 0:
                break
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 1

if len(dinheiro['Cedulas']) != 0:
    for i in dinheiro['Cedulas']:
        print(f'Cédulas de R${i[0]:3}: {i[1]:3.0f}')

if len(dinheiro['Moedas']) != 0:
    for i in dinheiro['Moedas']:
        print(f'Moedas de R${i[0]:3.2f}: {i[1]:3.0f}')
