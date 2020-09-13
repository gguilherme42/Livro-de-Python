import sys
import os
import os.path
# este módulo ajuda com a conversão de nomes de arquivos para links
# válidos em HTML
import urllib.request

mascara_do_estilo = "'margin: 5px 0px 5px %dpx;'"


def gera_estilo(nível):
    return mascara_do_estilo % (nível * 20)


def gera_listagem(página, diretório):
    nraiz = os.path.abspath(diretório).count(os.sep)
    for raiz, diretórios, arquivos in os.walk(diretório):
        nível = raiz.count(os.sep) - nraiz
        página.write("<p style=%s>%s</p>" % (gera_estilo(nível), raiz))
        estilo = gera_estilo(nível+1)
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            tamanho = os.path.getsize(caminho_completo)
            link = urllib.request.pathname2url(caminho_completo)
            página.write("<p style=%s><a href='%s'>%s</a>  (%d bytes)</p>" % (estilo, link, a, tamanho))


if len(sys.argv)<2:
    print("Digite o nome do diretório para coletar os arquivos!")
    sys.exit(1)

diretório = sys.argv[1]

página = open("arquivos.html","w", encoding = "utf-8")
página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
página.write("Arquivos encontrados a partir do diretório: %s" % diretório)
gera_listagem(página, diretório)
página.write("""
</body>
</html>
""")
página.close()
