import sqlite3
with sqlite3.connect('brasil.db') as conexao:
    conexao.row_factory = sqlite3.Row
    # Ordem decrescdente de Estados pela população.
    for estado in conexao.execute('select * from estados order by população desc'):
        print(f'''
      * {estado['id']}º 
        Estado: {estado['nome']}  | Sigla: {estado['sigla']}
        Região: {estado['regiao']}
        População: {estado['população']}
        ''')
