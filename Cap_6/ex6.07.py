n = input('Digite uma expressão somente com parênteses: ').strip()
lista = []
resp = False
for i in n:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if lista:
            lista.pop(-1)
        else:
            lista.append(i)

print('OK!' if not lista else 'Errado!')

