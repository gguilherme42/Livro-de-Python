def exerc(l):
    for x in l:
        if not(type(x) == list):
            print(x)
        else:
            return exerc(x)
# Obs: Está função só funciona nos casos em que a lista está como a declarada.


L = [1, [2, 3, 4, [5, 6, [7, 8, 9, 10]]]]
exerc(L)
