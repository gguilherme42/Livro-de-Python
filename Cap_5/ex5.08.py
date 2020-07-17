n1 = abs(int(input('Número: ')))
n2 = abs(int(input('Número: ')))
c = resultado = 0

while c < n2:
    resultado += n1
    c += 1
print(f'{n1} x {n2} = {resultado}')
