def comparaLista(s, lista):
    try:
        b = lista.index(s)
        return True
    except:
        return False


palavras = ['a', 'b', 'c', 'd', 'e']
print(comparaLista('f', palavras))
