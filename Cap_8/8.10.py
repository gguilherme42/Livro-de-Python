def fibonacci(n):
    fibo = 1
    while n > 1:
        fibo *= n
        n -= 1
    return fibo


print(fibonacci(5))
