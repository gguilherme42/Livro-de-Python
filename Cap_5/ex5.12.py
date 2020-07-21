soma = 0
for i in range(5):
    if i == 0:
        d = float(input('Valor do depósito inicial: R$'))
        j = float(input('Taxa de juros: '))
    else:
        d = float(input('Valor do depósito: R$'))
    valorJ = j * d / 100
    soma += valorJ + d
    print(f'{i + 1}º: R${soma:.2f}')
