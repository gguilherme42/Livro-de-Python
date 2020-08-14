def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def mmc(a, b):
    return abs(a * b) / mdc(a, b)


print(mmc(12, 45))
print(mdc(12, 45))
