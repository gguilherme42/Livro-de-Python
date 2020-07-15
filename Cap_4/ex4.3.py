l = [int(input(f'Número {i + 1}: ')) for i in range(3)]
print(f'O maior número é {max(l)} e o menor é {min(l)}')

# Outru modo:
# a, b, c = int(input('Número: ')), int(input('Número: ')), int(input('Número: '))
# if a > b and a > c:
#     if b > c:
#         print(f'Maior número é {a} e o menor número é {c}')
#     else:
#
#         print(f'Maior número é {a} e o menor número é {b}')
#
# elif b > a and b > c:
#     if a > c:
#         print(f'Maior número é {b} e o menor número é {c}')
#     else:
#
#         print(f'Maior número é {b} e o menor número é {a}')
# else:
#     if a > b:
#         print(f'Maior número é {c} e o menor número é {b}')
#     else:
#
#         print(f'Maior número é {c} e o menor número é {a}')

