import sqlite3
from contextlib import closing

nome = input('Nome do produto: ').lower().capitalize()

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute('SELECT * FROM Precos WHERE nome_produto = ?', (nome,))
        registro = cursor.fetchone()
        if not(registro is None):
            print(f'Nome: {registro[0]} | Preço: R${registro[1]:.2f}')
            valor = float(input('Novo valor: R$'))
            cursor.execute('UPDATE Precos SET preco = ? WHERE nome_produto = ?', (valor, registro[0]))
            if cursor.rowcount == 1:
                conexao.commit()
                print('Alteração gravada.')
            else:
                conexao.rollback()
                print('Alteração abortada.')
        else:
            print(f'Produto {nome} não encontrado.')