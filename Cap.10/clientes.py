class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    global c, c1

    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    def resumo(self):
        print(f'''
        Número: {self.numero}
        Nome: {c.nome} | Telefone: {c.telefone}
        Saldo: R${self.saldo:.2f}
        ''')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print(f'Saldo insuficiente para saque de R${valor:.2f}')
            self.operacoes.append(['SAQUE', valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC Nº {self.numero}')
        for o in self.operacoes:
            print(f'{o[0]:5}: R${o[1]:5.2f}')
        print(f'Saldo: {self.saldo:5.2f}')


c = Cliente('Guilherme', 1111)
c1 = Cliente('Viviane', 3333)
conta1 = Conta(c.nome, 1, 500)
conta2 = Conta(c1.nome, 2, 1000)
conta1.resumo()
conta1.saque(600)
conta1.resumo()
conta2.resumo()
conta2.saque(200)
conta2.resumo()
