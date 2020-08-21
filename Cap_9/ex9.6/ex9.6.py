largura = 70
entrada = open('entrada.txt', 'r')
for linha in entrada.readlines():
    if linha[0] == ';':
        continue
    elif linha[0] == '>':
        print(linha[1:].rjust(largura))
    elif linha[0] == '*':
        print(linha[1:].center(largura))
    elif linha[0] == '=':
        print(f'{linha[1:]}\n' * 40)
    elif linha[0] == '.':
        input('Digite algo para continuar. ')
        print()
    else:
        print(linha)
entrada.close()

