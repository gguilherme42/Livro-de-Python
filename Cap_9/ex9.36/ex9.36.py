import sys
import os
import os.path
import math

# Esta função converte o tamanho
# em unidades mais legíveis, evitando
# retornar e imprimir valores muito grandes.
def tamanho_para_humanos(tamanho):
    if tamanho == 0:
        return "0 byte"
    grandeza = math.log(tamanho, 10)
    if grandeza < 3:
        return "%d bytes" % tamanho
    elif grandeza < 6:
        return "%7.3f KB" % (tamanho / 1024.0)
    elif grandeza < 9:
        return "%f MB" % (tamanho / pow(1024,2))
    elif grandeza < 12:
        return "%f GB" % (tamanho / pow(1024,3))

mascara_do_estilo = "'margin: 5px 0px 5px %dpx;'"

def gera_estilo(nível):
    return mascara_do_estilo % (nível * 30)

# Retorna uma função, onde o parâmetro nraiz é utilizado
# para calcular o nível da identação
def gera_nível_e_estilo(raiz):
    def nivel(caminho):
        xnivel = caminho.count(os.sep) - nraiz
        return gera_estilo(xnivel)
    nraiz = raiz.count(os.sep)
    return nivel

# Usa a os.walk para percorrer os diretórios
# E uma pilha para armazenar o tamanho de cada diretório
def gera_listagem(página, diretório):
    diretório = os.path.abspath(diretório)
    # identador é uma função que calcula quantos níveis
    # a partir do nível de diretório um caminho deve possuir.
    identador = gera_nível_e_estilo(diretório)
    pilha = [ [diretório, 0]  ] # Elemento de guarda, para evitar pilha vazia
    for raiz, diretórios, arquivos in os.walk(diretório):
        # Se o diretório atual: raiz
        # Não for um subdiretório do último percorrido
        # Desempilha até achar um pai comum
        while not raiz.startswith(pilha[-1][0]):
            último = pilha.pop()
            página.write("<p style=%s>Tamanho: (%s)</p>" % (identador(último[0]), tamanho_para_humanos(último[1])))
            pilha[-1][1]+=último[1]
        página.write("<p style=%s>%s</p>" % (identador(raiz), raiz))
        d_tamanho=0
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            d_tamanho += os.path.getsize(caminho_completo)
        pilha.append( [raiz, d_tamanho])
    # Se a pilha tem mais de um elemento
    # os desempilha
    while len(pilha)>1:
            último = pilha.pop()
            página.write("<p style=%s>Tamanho: (%s)</p>" % (identador(último[0]), tamanho_para_humanos(último[1])))
            pilha[-1][1]+=último[1]


if len(sys.argv)<2:
    print("Digite o nome do diretório para coletar os arquivos!")
    sys.exit(1)

diretório = sys.argv[1]

página = open("tarquivos.html","w", encoding = "utf-8")
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