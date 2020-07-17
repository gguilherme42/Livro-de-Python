dividendo = abs(int(input('Número: ')))
divisor = abs(int(input('Número: ')))
c = somadivisor = 0

while somadivisor < dividendo:
    somadivisor += divisor
    c += 1
resto = dividendo - (somadivisor - divisor) if (somadivisor > dividendo) else dividendo - somadivisor
#Para ajustar o valor do resto da divisão verifica-se se a soma do divisor é maior que o dividendo,
#caso seja, o resto recebera a soma do divisor menos o divindendo menos o divisor.
print(f'''{dividendo} / {divisor} = {c}
{dividendo} % {divisor} = {resto}''')

