class Televisao:
    def __init__(self, marc, t):
        self.ligada = False
        self.canal = 0
        self.marca = marc
        self.tamanho = t


tvSony = Televisao('Sony', '44x30cm')

tvSamsung = Televisao('Samsung', '60x45cm')
tvSamsung.ligada = True
tvSamsung.canal = 12
print(f'Marca da televisão: {tvSony.marca} | Tamanho: {tvSony.tamanho}  '
      f'Ligada: {"Sim" if tvSony.ligada else "Não"} | Canal: {"Nenhum" if tvSony.canal == 0 else tvSony.canal}')

print(f'Marca da televisão: {tvSamsung.marca} | Tamanho: {tvSamsung.tamanho}  '
      f'Ligada: {"Sim" if tvSamsung.ligada else "Não"} | Canal: {"Nenhum" if tvSamsung.canal == 0 else tvSamsung.canal}')