feriados = [['2020-01-01', 'Confraternização Universal'], ['2014-04-21', 'Tiradentes'],
            ['2020-05-01', 'Dia do Trabalhador'], ['2014-09-07', 'Independência'],
            ['2020-10-12', 'Padroeira do Brasil'], ['2014-11-02', 'Finados'],
            ['2020-11-15', 'Proclamação da República'], ['2013-12-25', 'Natal']]
# Data no formato ISO 8601: ANO-MÊS-DIA

import sqlite3
import datetime
hoje = datetime.date.today()
hoje60dias = hoje + datetime.timedelta(days=180)

# Criação da tabela
# with sqlite3.connect('brasil.db', detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
#     conexao.execute('''
#     create table feriados(id integer primary key autoincrement,
#     data date, descrição text)
#     ''')
#     conexao.executemany('insert into feriados (data, descrição) values(?,?)', feriados)

with sqlite3.connect('brasil.db', detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    for feriado in conexao.execute('select * from feriados where data >= ?  and data <= ?', (hoje, hoje60dias)):
        print(f'- {feriado["data"].strftime("%d/%m")} {feriado["descrição"]}')
