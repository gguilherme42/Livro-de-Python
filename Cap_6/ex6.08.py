lista = list(range(100))
p = int(input('Digite um número para procurar na lista: '))
x = 0
while x < len(lista):
    if lista[x] == p:
        print(f'Valor encontrado na posição {x}')
        break
    x += 1
    if x == len(lista):
        print('Valor não encontrado!')
