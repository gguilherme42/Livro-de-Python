
c = ('\033[m',          # 0 - Fundo e letras padrão.
     '\033[1;30m',     # 1 - Letra em negrito e branca, fundo padrão
     '\033[1;31m',     # 2 - Letra em negrito e vermelha, fundo padrão
     '\033[1;32m',     # 3 - Letra em negreito e verde, fundo padrão
     '\033[1;33m',     # 4 - Letra em negreito e amarela, fundo padrão
     '\033[1;34m',     # 5 - Letra em negreito e azul, fundo padrão
     '\033[1;35m',     # 6 - Letra em negreito e margenta, fundo padrão
     '\033[1;36m',     # 7 - Letra em negreito e ciano, fundo padrão
     '\033[1;37m',     # 8- Letra em negreito e cinza, fundo padrão
     '\033[1;30;44m',   # 9 - Fundo azul, letras brancas em negrito.
     '\033[1;30;43m',   # 10 - Fundo amarelo, letras brancas em negrito.
     '\033[1;30;7m')    # 11 - Fundo branco, letras pretas em negrito.


def cor(msg, color=0):
    global c
    return f'{c[color]}{msg}{c[0]}'


def mat1(m):
     for l in m:
          for c in l:
               print(f'| {c} ', end='| ')
          print()


def empate(m):
     emp = bool
     for l in m:
          for c in l:
               if c == '-':
                    emp = False
               else:
                    emp = True
     return emp
