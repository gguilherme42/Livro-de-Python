d = float(input('Qual a distância que deseja percorrer em Km? '))
preco = d * 0.5 if d <= 200 else d * 0.45
print(f'Preço: R${preco:.2f}')
