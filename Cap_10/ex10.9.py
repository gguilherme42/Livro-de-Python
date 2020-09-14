from Cidades import Cidade
from Estados import Estado


sl = Cidade('São Leopoldo', 340050)
poa = Cidade('Porto Alegre', 400000)
sapuc = Cidade('Sapucaia', 190000)

rs = Estado('Rio Grande do Sul', 'RS', [sl, poa, sapuc])
rs.resumo()


ar = Cidade('Angra dos Reis', 300520)
db = Cidade('Duas Barras', 3024012)
co = Cidade('Cordeiro', 310231)

rj = Estado('Rio de Janeiro', 'RJ', [ar, db, co])
rj.resumo()


os = Cidade('Osasco', 1231415)
bu = Cidade('Bauru', 123111)
ji = Cidade('Jundiaí', 5134526)
sp = Estado('São Paulo', 'SP', [os, bu, ji])
sp.resumo()
