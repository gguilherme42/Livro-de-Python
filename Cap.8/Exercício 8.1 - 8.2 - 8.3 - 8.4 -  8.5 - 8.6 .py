'''
Ex. 8.1 - 8.2 - 8.3 - 8.4 - 8.5 - 86:
    pág.163 - 167
'''

# Ex. 8.1
def mai(m=0, n=0):
    mai = 0
    if m > n:
        mai = m
    else:
        mai = n
    return mai

# Ex. 8.2
def multp(n1=0, n2=0):
    r = False
    while n1 < n2:
        if n1 == n2:
            r = True
        n1 *= n1
    return r

# Ex. 8.3
def area(l=0, c=0):
    a = l * c
    return a

# Ex. 8.4
def areaR(h=0, b=0):
    a = (b * h) / 2
    return a


# Ex. 8.5
def pesqL(*l, v=0):
    for i, e in enumerate(l):
        if e == v:
            return i
    return None


# Ex. 8.6
def soma(*l):
    tot = 0
    for v in l:
        tot += v
    return tot
