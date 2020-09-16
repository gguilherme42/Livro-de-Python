import sqlite3
from contextlib import closing

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute('SELECT preco FROM Precos')
        registros = cursor.fetchall()
        for r in registros:
            print(f'Preço: R${r[0]:.2f}')
