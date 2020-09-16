import sqlite3
from contextlib import closing

v1 = float(input('valor 1: '))
v2 = float(input('valor 2: '))

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute('SELECT * FROM Precos WHERE preco BETWEEN ? AND ? ORDER BY preco', (v1, v2))
        registros = cursor.fetchall()
        for r in registros:
            print(f'Nome: {r[0]} | Preço: R${r[1]:.2f}')
