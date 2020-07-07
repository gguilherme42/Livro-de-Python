'''
Ex. 11.5
    Escreva um programa que aumente o preço de todos os produtos do banco
    preços.db em 10%.
'''
import sqlite3
from contextlib import closing
with sqlite3.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        # Preços antigos
        cursor.execute('select * from preços')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'> Produto: {resultado[0]} - Preço: R$ {resultado[1]:.2f}\n')
        # Aumento dos preços
        cursor.execute('select * from preços')
        while True:
            resultado = cursor.fetchall()
            if resultado is None:
                break
            else:
                for l in resultado:
                    aum = (l[1] * 10) / 100
                    p = l[1] + aum
                    cursor.execute('''
                            update preços 
                            set preco = ? 
                            where produto = ? 
                            ''', (p, l[0]))
                    print('Registros alterados: ', cursor.rowcount)
                    if cursor.rowcount == 1:
                        conexao.commit()
                        print('Alterações gravadas!')
                    else:
                        conexao.rollback()
                        print('Alterações abortadas!')


