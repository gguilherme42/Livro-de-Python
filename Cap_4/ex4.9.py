casa = float(input('Valor da casa: R$'))
anos = int(input('Anos a pagar: '))
salario = float(input('Salário: R$'))
prestacao = casa / anos
prestacao_no_sal = (prestacao * 100) / salario
print('Aprovado o empréstimo!' if prestacao_no_sal <= 30 else 'Reprovado o empréstimo!')
