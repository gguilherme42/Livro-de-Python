def valida_string(s="string", min=1, max=30):
    return True if min < len(s) < max else False


print(valida_string('Ta certo? '))