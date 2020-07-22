notas = [int(input(f'Nota {i + 1}: ')) for i in range(7)]
print(f'Média: {sum(notas)/ len(notas):.2f}')
