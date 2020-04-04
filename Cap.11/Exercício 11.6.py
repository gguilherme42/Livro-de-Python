'''
Ex. 11.6:
    Escreva um programa que pergunte o nome do produto e um novo preço.
    Usando o banco preços.db, atualize o preço deste produto no bando de dados.
'''
import sqlite3
from contextlib import closing
with sqlite3.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        produto = str(input('Nome do produto: '))
        p = float(input('Preço: R$'))
        cursor.execute('''
        insert into preços (produto, preco) 
        values (?, ?)
        ''', (produto, p))
        cursor.execute('select * from preços')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'> Nome: {resultado[0]} - Preço: R${resultado[1]:.2f}\n')
