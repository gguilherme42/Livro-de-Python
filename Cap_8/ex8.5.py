def pesquisa(lista, valor):
    try:
        return lista.index(valor)
    except:
        return None


lista = [1, 2, 4, 5, 6]
print(f'{pesquisa(lista, 1)}')