# Porque nem sempre se sabe a quantidade de repetições.
l = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    l.append(n)

if l:
    for i in l:
        print(i)