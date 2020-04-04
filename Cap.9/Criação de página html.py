'''
Exercício 9.30:
    Modifique o programa da listagem 9.10 para gerar uma lista html,
    usando os elemtnos ul e li. Todos os elementos da lista devem estar dentro do
    elemento ul, e cada item dentro de um elemento li. Exemplo:
    <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>
'''
filmes = {
    'Drama': ['Cidadão Kane', 'O Poderoso Chefão'],
    'Comédia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'Policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'Guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!'],
}


pagina = open('página.html', 'w', encoding='utf-8')
pagina.write(f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>BOM DIA!</title>
</head>
<body>
<h1>FILMES</h1>
''')
for k, v in filmes.items():
    pagina.write(f'<h2>{k.upper()}</h2>')
    pagina.write(f'<ul>')
    for e in v:
        pagina.write(f'<li>{e}</li>')
    pagina.write(f'</ul>')
pagina.write('''
</body>
</html>
''')
pagina.close()
