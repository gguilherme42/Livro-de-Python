import sqlite3
print('='*80)
print('REGIÃO   ESTADOS   POPULAÇÃO -> MÍNIMA     MÁXIMA      MÉDIA       TOTAL')
print('='*80)
with sqlite3.connect('brasil.db') as conexao:
    for regiao in conexao.execute('''
    select regiao, count(*), min(população), max(população), 
    avg(população), sum(população) 
    from estados
    group by regiao
    order by sum(população) desc
    '''):
        print(f'{regiao[0]:6} {regiao[1]:6} {regiao[2]:25,} {regiao[3]:10,} {regiao[4]:10,.0f} {regiao[5]:13,}')
    print('-'*80)
    print('BRASIL: {0:6} {1:23,} {2:10,} {3:10,.0f} {4:13,.0f}'.format(*conexao.execute('''
    select count(*), min(população), max(população), avg(população), sum(população) 
    from estados
    ''').fetchone()))
