def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)




