'''
Ex. 11.2:
    Faça um programa para listar todos o preços do banco
    preços.db.
'''
import sqlite3
from contextlib import closing
with sqlite3.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from preços')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'Produto: {resultado[0]}\nPreço: R${resultado[1]} ')
