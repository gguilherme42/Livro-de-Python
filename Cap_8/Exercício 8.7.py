'''
Ex. 8.7
'''


def mdc(b=0, a=0):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


#Ex. 8.8
def mmc(a, b):
    return (a * b) / mdc(a, b)


# Ex 8.9



# Ex. 8.10
