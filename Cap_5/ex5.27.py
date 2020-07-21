def palindrome(n):
    if n == n[::-1]:
        return True
    return False


print(palindrome(input('Digite um número: ').strip()))
