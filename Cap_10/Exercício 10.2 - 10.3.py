'''
Ex. 10.2:
    Atualmente, a classe Televisão inicializa com canal com 2.
    Modifique a classe Televisão forma a receber o canal inicial
    em seu construtor.

Ex. 10.3:
    Modifique a classe Televisão de forma que, se perdirmos para mudar
    o canal para baixo, além do mínimo, ela vá para o canal máximo. Se
    mudarmos o canal para cima, além do máximo, que volte ao canal mínimo.
'''
class Televisao:
    def __init__(self, min=0, max=10, canalinicial=0):
        self.ligada = True
        self.canal = canalinicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_cima(self):
        if self.canal == self.cmax:
            print(f'Canal: {self.canal}')
            self.canal = self.cmin
        elif (self.canal + 1) <= self.cmax:
            print(f'Canal: {self.canal}')
            self.canal += 1

    def muda_canal_para_baixo(self):
        if self.canal == self.cmin:
            print(f'Canal: {self.canal}')
            self.canal = self.cmax
        elif (self.canal - 1) >= self.cmin:
            print(f'Canal: {self.canal}')
            self.canal -= 1


tv = Televisao(1, 10, 1)
for x in range(1, 15):
    tv.muda_canal_para_baixo()
