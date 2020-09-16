import sqlite3
from contextlib import closing


with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute('SELECT * FROM Precos')
        registros = cursor.fetchall()
        for r in registros:
            print(f'Nome: {r[0]} | Preço: R${r[1]:.2f}')
            v10 = ((r[1] * 10)/100) + r[1]
            cursor.execute('UPDATE Precos SET preco = ? WHERE nome_produto = ?', (v10, r[0]))
            if cursor.rowcount == 1:
                conexao.commit()
                print('Alterações gravadas!')
                print(f'Novo preço: R${v10:.2f}\n')
            else:
                conexao.rollback()
                print('Alterações abortadas!')
