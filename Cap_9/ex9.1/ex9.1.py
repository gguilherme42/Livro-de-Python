import sys

if (len(sys.argv) != 2):  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-01.py nome_do_arquivo\n\n")
else:
    file = sys.argv[1]
    arquivo = open(f'{file}', 'r')
    for linha in arquivo.readlines():
         print(linha[:-1]) # Remove o último caractere da linha que é um Enter ou \n
arquivo.close()
