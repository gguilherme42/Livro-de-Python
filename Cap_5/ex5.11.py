d = float(input('Valor do depósito: R$'))
j = float(input('Taxa de juros da poupança: '))
valorJ = j * d / 100
soma = 0

for _ in range(24):
    soma += valorJ + d
    print(f'{_ + 1}º: R${soma:.2f}')
