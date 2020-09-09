import sys
import os
import os.path
# este módulo ajuda com a conversão de nomes de arquivos para links
# válidos em HTML
import urllib.request

if len(sys.argv)<2:
    print("Digite o nome do diretório para coletar os arquivos jpg e png!")
    sys.exit(1)

diretório = sys.argv[1]

pagina = open("imagens.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens PNG e JPG</title>
</head>
<body>
""")
pagina.write("Imagens encontradas no diretório: %s" % diretório)
for entrada in os.listdir(diretório):
    nome, extensão = os.path.splitext(entrada)
    if extensão in [".jpg",".png"]:
        caminho_completo = os.path.join(diretório, entrada)
        link = urllib.request.pathname2url(caminho_completo)
        pagina.write("<p><a href='%s'>%s</a></p>" % (link, entrada))

pagina.write("""
</body>
</html>
""")
pagina.close()
