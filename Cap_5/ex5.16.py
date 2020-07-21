# Se digitar zero o programa é finalizado.
v = int(input('Digite um valor: R$'))
c = vin = dez = cinco = um = 0
cedula = []
while True:
    if v == 0:
        break
    elif v >= 50:
        c = v // 50
        v -= c * 50
        cedula.append([50, c])
    elif v >= 20:
        vin = v // 20
        v -= vin * 20
        cedula.append([20, vin])
    elif v >= 10:
        dez = v // 10
        v -= dez * 10
        cedula.append([10, dez])
    elif v >= 5:
        cinco = v // 5
        v -= cinco * 5
        cedula.append([5, cinco])
    else:
        um = v
        v -= um
        cedula.append([1, um])

for i in cedula:
    print(f'Cédulas de R${i[0]:2}: {i[1]:2}')
