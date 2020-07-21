pontos = 0
for i in range(3):
    resp = input(f'Resposta da questão {i + 1}: ').lower().strip()[0]
    if i + 1 == 1 and resp == 'a':
        pontos += 1
    elif i + 1 == 2 and resp == 'b':
        pontos += 1
    elif resp == 'c':
        pontos += 1
print(f'Total de pontos: {pontos}')
