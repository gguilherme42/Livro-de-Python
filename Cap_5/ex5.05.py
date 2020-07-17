c = 0
x = 1
while c < 10:
    if x % 3 == 0:
        c += 1
        print(f'{c:2}º: {x}')
    x += 1
