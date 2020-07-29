s1 = input('String 1: ').upper()
s2 = input('String 2: ').upper()
print(f'Posição: {s1.find(s2)}' if s2 in s1 else 'A segunda não ocorre dentro da primeira.')
