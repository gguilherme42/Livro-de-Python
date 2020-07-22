def palindrome(n):
    return n == n[::-1]


print(palindrome(input('Digite um número: ').strip()))
