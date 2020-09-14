class Televisao:
    def __init__(self, marc, t, canal, cmin, cmax):
        self.ligada = False
        self.canal = canal
        self.marca = marc
        self.tamanho = t
        self.cmin = cmin
        self.cmax = cmax

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1


    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1


tvSony = Televisao('Sony', '44x30cm', 1, 1, 10)
tvSamsung = Televisao('Samsung', '60x45cm', 3, 1, 20)
tvSamsung.ligada = True
tvSamsung.canal = 12
print(f'Marca da televisão: {tvSony.marca} | Tamanho: {tvSony.tamanho}  '
      f'Ligada: {"Sim" if tvSony.ligada else "Não"} | Canal: {"Nenhum" if tvSony.canal == 0 else tvSony.canal}')

print(f'Marca da televisão: {tvSamsung.marca} | Tamanho: {tvSamsung.tamanho}  '
      f'Ligada: {"Sim" if tvSamsung.ligada else "Não"} | Canal: {"Nenhum" if tvSamsung.canal == 0 else tvSamsung.canal}')