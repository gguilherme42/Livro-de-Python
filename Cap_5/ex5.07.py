n = abs(int(input('Digite um número para ver sua tabuada: ')))
i = int(input('Digite o inicio: '))

while True:
    fim = int(input('Digite o fim: '))
    if fim <= i:
        print(f'Fim deve ser maior que o inicio')
    else:
        break

while i < fim:
    i += 1
    print(f'{n} x {i} = {n * i}')
