v = float(input('Digita a velocidade do carro em km/h: '))
if v > 80:
    ultrapassou = v - 80
    m = 5 * ultrapassou
    print(f'Multado! No valor de {m:.2f}')
else:
    print('Tudo certo!')
