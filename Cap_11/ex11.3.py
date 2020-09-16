import sqlite3
from contextlib import closing

nome = input('Nome do produtuo: ').lower().capitalize()

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute('SELECT * FROM Precos WHERE nome_produto = ?', (nome,))
        registros = cursor.fetchone()
        if registros is None:
            print(f'{nome} não encontrado!')
        else:
            for r in registros:
                print(f'Nome: {r[0]} | Preço: R${r[1]:.2f}')
