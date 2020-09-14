class Televisao:
    def __init__(self, marc, t, canal, cmin=2, cmax=14):
        self.ligada = False
        self.canal = canal
        self.marca = marc
        self.tamanho = t
        self.cmin = cmin
        self.cmax = cmax

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


tv1 = Televisao('Sony', '60x40cm', 0, cmin=1, cmax=30)
tv2 = Televisao('Sony', '70x50cm', 0, cmin=3, cmax=40)
