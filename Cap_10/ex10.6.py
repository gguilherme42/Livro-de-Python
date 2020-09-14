from Clientes import Cliente
from Contas import Conta
Cleiton = Cliente('Cleiton Roberto', '99357-8351')
Joana = Cliente('Joana Silveira', '99047-2741')
contaC = Conta([Cleiton], 1, 500)
contaJ = Conta([Joana], 2, 2000)


contaC.resumo()
contaC.saque(450)
contaC.saque(100)
contaC.extrato()

contaJ.resumo()
contaJ.deposito(300)
contaJ.extrato()
