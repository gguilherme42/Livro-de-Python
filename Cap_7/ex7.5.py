s1 = input('String 1: ').upper().strip()
s2 = input('String 2: ').upper().strip()
for i in s1:
    if i not in s2:
        print(f'{i}', end='')
