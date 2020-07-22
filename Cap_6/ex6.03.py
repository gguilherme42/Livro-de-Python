conjunto = list(set([input('Digite algo para lista A: ') for i in range(3)] +
           [input('Digite algo para a lista B: ') for c in range(3)]))
print(conjunto)

# Outra maneira de fazer:
duaslistas = [input('Digite algo para lista A: ') for i in range(3)] + \
           [input('Digite algo para a lista B: ') for c in range(3)]

terceiralista = []
for i in duaslistas:
    if not terceiralista:
        terceiralista.append(i)
    else:
        if i not in terceiralista:
            terceiralista.append(i)

print(terceiralista)