# Quando um valor for igual à outro, eles não iram trocar de posição.

lista = [3, 3, 1, 5, 4]
fim = len(lista)
while fim > 1:
    trocou = False
    for i in range(fim - 1):
        if lista[i] > lista[i + 1]:
            trocou = True
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp
    if not trocou:
        break
    fim -= 1

print(lista)
