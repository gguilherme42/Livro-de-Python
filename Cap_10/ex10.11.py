class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f'CC Nº: {self.numero}')
        for c in self.clientes:
            print(f'    - Nome: {c.nome} | Tel.:{c.telefone}')
        print(f'    - Saldo: R$ {self.saldo:.2f}')

    def saque(self, valor):
        from datetime import date
        from Modulos import Cores
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor, date.today()])
            return True
        else:
            print(f'{Cores.colorir("Saque negado! Saldo insuficiente.", "r")}')
            return False

    def deposito(self, valor):
        from datetime import date
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor, date.today()])

    def extrato(self):
        print(f'Extrato CC Nº: {self.numero}\n')
        for v in self.operacoes:
            print(f'{v[0]}: R${v[1]:.2f} - {v[2]}')
        print(f'\n      Saldo: R${self.saldo:.2f}\n')


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        from datetime import date
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor, date.today()])
            return True
        return False

    def extrato(self):
        print(f'Extrato CC Nº: {self.numero}\n')
        for v in self.operacoes:
            print(f'{v[0]}: R${v[1]:.2f} - {v[2]}')
        print(f'\n      Saldo: R${self.saldo:.2f}\n')
        print(f'        Limite: R$ {self.limite:.2f} ')
        print(f'        Disponível para saque: R$ {(self.limite + self.saldo):.2f} ')

