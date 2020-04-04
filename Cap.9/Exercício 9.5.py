'''
Ex. 9.5:
    Crie um programa que inverta a ordem das linhas dos arquivos pares.txt.
    A primeira linha deve conter o maior número; e a última, o menor.
'''
lista = []
for n in range(0, 51):
    if n % 2 == 0:
        lista.append(n)
# Lista de pares decrescente
paresI = sorted(lista, reverse=True)
print(paresI)

# Criação do arquivo
paresd = open('paresD.txt', 'w')
for n in paresI:
    paresd.write(f'{n} ')
paresd.close()
