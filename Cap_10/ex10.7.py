from Clientes import Cliente
from Contas import Conta
Maria = Cliente('Maria', '99475-2233')
contaM = Conta([Maria], 3, 250)

contaM.resumo()