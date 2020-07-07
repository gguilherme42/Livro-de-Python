'''
Ex. 11.3:
    Escreva um programa que realize as consultas do banco de dados
    preços.db, criado no exercício 11.1. O programa deve perguntar
    o nome do produto e listar seu preço.
'''
import sqlite3
from contextlib import closing

produto = str(input('Nome do 1º produto: '))
produto2 = str(input('Nome do 2º produto: '))
with sqlite3.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from preços where produto = ?', (produto,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print('1º produto não encontrado.')
                break
            print(f'Nome: {resultado[0]}\nPreço: {resultado[1]}\n')
            x += 1
        cursor.execute('select * from preços where produto = ?', (produto2,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print('2º produto não encontrado.')
                break
            print(f'Nome: {resultado[0]}\nPreço: {resultado[1]}\n')
            x += 1
