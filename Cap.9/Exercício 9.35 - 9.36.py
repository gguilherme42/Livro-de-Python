'''
Ex. 9.35 - 9.36:
    Utilizando a função os.walk, crie uma página HTML com o nome,
    tamanho e espaço ocupado de um diretório passado e de seus subdiretórios.
'''
import os
pagina2 = open('pagina2.html', 'w', encoding='utf-8')
pagina2.write('''
<!DOCTYPE html>
<html lang="pt-Br">
<head>
<meta charset="utf-8">
<title>DOCUMENTOS</title>
</head>
<body>
''')
for r, diretorios, arquivos in os.walk('/home/atem/PycharmProjects/Livro/Cap.9'):
    pagina2.write(f'<h2>Caminho: {r}</h2>')
    for d in diretorios:
        pagina2.write(f'<h3>* {d}/</h3>')
        for a in arquivos:
            pagina2.write(f'<h4> - {a}</h4>')
    pagina2.write(f'<p>Diretórios: {len(diretorios)}</p>')
    pagina2.write(f'<p>Arquivos: {len(arquivos)}</p>')
    pagina2.write(f'<p>Tamanho: {os.path.getsize(r)}</p>')
pagina2.write('''
</body>
</html>
''')
pagina2.close()
