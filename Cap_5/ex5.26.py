d = int(input('Digite o dividendo: '))
div = int(input('Digite o divisor: '))
valord = d
resp = 0
while div <= valord:
    valord -= div
    resp += 1
print(f'{d} // {div} = {resp}')
