import sqlite3
from contextlib import closing
dados = [('Shampoo', 8.9), ('Chocolate', 4.5),
         ('Cerveja', 7.3), ('Água', 3.2),
         ('Salgadinho', 5.0), ('Carne', 22.8)]

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Precos (
            nome_produto text,
            preco decimal)
        ''')

        cursor.executemany('''
        INSERT INTO Precos (nome_produto, preco)
        VALUES (?, ?)
        ''', (dados))
        conexao.commit()

        cursor.execute('SELECT * FROM Precos')
        registros = cursor.fetchall()
        for r in registros:
            print(f'`Produto: {r[0]} | Preço: R${r[1]:.2f}')
