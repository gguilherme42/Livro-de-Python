dados = [['SP', 'SE', 'São Paulo'], ['MG', 'SE', 'Minas Gerais'],
         ['RJ', 'SE', 'Rio de Janeiro'], ['BH', 'NE', 'Bahia'],
         ['PR', 'S', 'Paraná'], ['RS', 'S', 'Rio Grande do Sul'],
         ['PE', 'NE', 'Pernambuco'], ['CE', 'NE', 'Ceará'],
         ['PA', 'N', 'Pará'], ['SC', 'S', 'Santa Catarina']]

import sqlite3
with sqlite3.connect('brasil.db') as conexao:
    # Adicionando a sgila e a região para a tabela estados
    # conexao.execute('alter table estados add sigla text')
    # conexao.execute('alter table estados add regiao text')

    # Adicionando a sigla e região de cada Estado
    conexao.executemany('''
    update estados
    set sigla = ?, regiao = ?
    where nome = ?
    ''', dados)
