from Clientes import Cliente
from Contas import Conta
Joao = Cliente('João', '99475-2233')
Jose = Cliente('José', '99475-2233')
contaJJ = Conta([Joao, Jose], 3, 500)

contaJJ.resumo()
