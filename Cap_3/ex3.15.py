cig = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Quantidade de anos que fuma: '))
anosPerdidos = (cig * ((10 / 3600) / 24) * (anos * 365 * 24)) / 24
print(f'Dias de vida perdidos: {anosPerdidos:.1f} dia(s)')
