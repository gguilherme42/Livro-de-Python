import os.path
if os.path.exists('z'):
    if os.path.isdir('z'):
        print(f'"z" existe e é um diretório.')
    else:
        print(f'"z" existe e nãoe é um diretório.')
