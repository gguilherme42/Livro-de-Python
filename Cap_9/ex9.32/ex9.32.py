import os.path, sys

name = sys.argv[1]
if os.path.exists(name):
    if os.path.isdir(name):
        print(f'"{name}" existe e é um diretório')
    else:
        print(f'"{name}" existe e é um arquivo')
