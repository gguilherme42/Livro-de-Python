n = int(input('Digite um número para calcular sua raiz: '))
b = 2
while True:
    p = (b + (n / b)) / 2
    res = p ** 2
    b = p
    if abs(n - res) < 0.0001:
        break

print(f'p = {p}')
print(f'p² = {res}')
