s1 = input('String 1: ').upper().strip()
s2 = input('String 2: ').upper().strip()
s3 = input('String 3: ').upper().strip()
for l1 in s1:
    if l1 not in s2:
        print(l1, end='')
    else:
        print(s3, end='')

