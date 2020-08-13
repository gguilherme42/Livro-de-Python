def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


maior = lambda x, y: x if x > y else y
menor = lambda x, y: x if x < y else y
print(mdc(maior(27, 9), menor(27, 9)))

