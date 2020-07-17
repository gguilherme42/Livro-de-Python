x = 1
while True:
    n = int(input('Digite um número: '))
    #pega o valor absoluto do número inteiro
    if n > 0:
        break
    else:
        print('Digite um número maior que zero.')

while x <= n:
    if x % 2 != 0:
        print(x)
    x += 1
