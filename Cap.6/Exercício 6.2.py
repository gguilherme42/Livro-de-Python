'''
Ex 6.2:
    Faça um programa que leia duas listas e que gere uma
    terceira com os elementos das duas primeiras
'''

l=[]
b = []
for c in range(0, 5):
    l.append(int(input('Digite um número para lista l: ')))
    b.append(int(input('Digite um número para lista b: ')))
c = [[l[:]], [b[:]]]
print(l)
print(b)
print(c)