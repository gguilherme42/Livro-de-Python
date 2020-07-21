soma = cont = 0
while True:
    n = int(input('Digite um número inteiro ou 0 para sair: '))
    soma += n
    cont += 1
    if n == 0:
        break
print(f'Total de números digitados: {cont}')
print(f'Soma dos números digitados: {soma}')
print(f'Média aritimética: {soma / cont:.2f}')

