# Lista de 10 Estados brasileiros.
# Link: https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o
dados = [['São Paulo', 45919049], ['Minas Gerais', 21168791],
         ['Rio de Janeiro', 17264943], ['Bahia', 14873064],
         ['Paraná', 11433957], ['Rio Grande do Sul', 11377239],
         ['Pernambuco', 9558071], ['Ceará', 9132078],
         ['Pará', 8602865], ['Santa Catarina', 7164788]]
import sqlite3
from contextlib import closing
with sqlite3.connect('brasil.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
        create table estados(
        id integer primary key autoincrement,
        nome text,
        população integer
        )
        ''')
        cursor.executemany('''
        insert into estados(nome, população) values(?, ?)
        ''', dados)
        conexao.commit()
