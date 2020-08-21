import sys

if (len(sys.argv) != 4):  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-01.py nome_do_arquivo inicio fim\n\n")
else:
    file = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(f'{file}', 'r')
    for linha in arquivo.readlines()[inicio - 1: fim]:
         print(linha[:-1]) # Remove o último caractere da linha que é um Enter ou \n
    arquivo.close()
