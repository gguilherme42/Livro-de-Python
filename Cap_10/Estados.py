class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.populacao = 0
        self.popula_estado(cidades)

    def resumo(self):
        print(f'''
Nome: {self.nome} - {self.sigla}  
Cidades: {len(self.cidades)} 
População: {self.populacao}''')

    def popula_estado(self, cidades):
        for c in cidades:
            self.cidades.append(c)
            self.populacao += c.populacao

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)
        self.populacao += cidade.populacao
