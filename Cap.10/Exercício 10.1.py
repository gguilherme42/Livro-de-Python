'''
Ex. 10.1:
    Adicione os atributos tamanho e marca à clase Televisão.
    Crie dois objetos Televisão e atribua tamanhos e marcas
    diferentes. Depois, imprima o valor desses atributos de
    forma a confirmar a independência dos valores de cada
    instância (objeto).
'''
class Televisao:
    def __init__(self):
        self.ligada = True
        self.canal = 2
        self.tamanho = '30x40cm'
        self.marca = 'Sony'

tv1 = Televisao()
tv2 = Televisao()
tv2.marca = str(input('Qual a marca da TV? '))
tv2.canal = int(input('Qual o canal que a TV está ligada? '))
print(f'''
Marca: {tv1.marca}
Tamanho: {tv1.tamanho}
Ligada: {tv1.ligada}
Canal = {tv1.canal}
''')
print(f'''
Marca: {tv2.marca}
Tamanho: {tv2.tamanho}
Ligada: {tv2.ligada}
Canal = {tv2.canal}
''')
