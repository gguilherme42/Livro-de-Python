notas = [int(input(f'Nota {i + 1}: ')) for i in range(3)]
print("Aprovado!" if (sum(notas) / len(notas)) > 7 else "Reprovado!")
