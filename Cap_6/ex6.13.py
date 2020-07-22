t = [-10, -8, 0, 1, 2, 5, -2, -4]
min = max = t[0]
for i in t:
    if i < min:
        min = i
    if i > max:
        max = i
print(f'Menor: {min} | Maior: {max}')
