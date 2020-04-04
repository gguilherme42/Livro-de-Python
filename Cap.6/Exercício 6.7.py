'''
Ex 6.7:
    Faça um programa que leia uma expressão com
    parênteses. Usando pilhas, verificque se os
    parênteses foram abertos e fechados na ordem correta.
'''
exp = str(input('Digite uma expressão: ')).strip()
x = []
for i, v in enumerate(exp):
    if exp[i] == '(':
        x.append(exp[i])
    elif exp[i] == ')':
        if x != []:
            x.pop(0)
if x != []:
    print(x)
    print('Expressão inválida!')
else:
     print('Expressão válida!')
