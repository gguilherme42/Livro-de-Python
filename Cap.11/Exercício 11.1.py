'''
Ex. 11.1:
    Faça um prograam que crie o banco de dados preços.db com a tabela
    preços para armazenar uma lista de preços de venda de produtos. A
    tabela deve conter o nome do produto e seu respectivo preço. O programa
    também deve inserir alguns dados para test.
'''
import sqlite3
# Importando o closing para o cursor
from contextlib import closing
with sqlite3.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
            create table preços(produto text, preco real)
        ''')
        cursor.execute('''
            insert into preços(produto, preco) values(?, ?)
        ''', ('Pera', 2.5))
        cursor.execute('''
            insert into preços(produto, preco) values(?, ?)
        ''', ('Maça', 1.5))
        cursor.execute('''
            insert into preços(produto, preco) values(?, ?)
        ''', ('Limão', 1))
        conexao.commit()
