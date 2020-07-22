# Percorre a lista uma vez, se ela estiver ordenada, pois como está ordenanda,
# não há elementos para trocar de posição.

lista = [1, 2, 3, 4, 5]
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
