agenda = []
gravada = lida = False


def mostra_dados(n, t, e, d):
    print(f'Nome: {n} | Telefone: {t} | Email: {e} | Nascimento: {d}')


def confirma(string):
    while True:
        try:
            r = string.lower().strip()[0]
        except:
            print('Resposta Inválida.')
        else:
            if r == 's':
                return True
            elif r == 'n':
                return False
            else:
                print('Resposta Inválida.')


def verifica_input(r):
    return None if '#' in r else r


def pede_algo(palavra='', opcional=''):
    while True:
        try:
            resp = input(f'{palavra}: ')
        except:
            print('Erro!')
        else:
            if opcional and resp == '':
                return opcional
            if verifica_input(resp) and not pesquisa_nome(resp): #Se o nome/telefone não contém '#' e não é repetido
                return resp
            print(f'Digite um {palavra} válido.')


def pesquisa_nome(nome):
    global agenda
    nome_min = nome.lower().strip()
    for p, e in enumerate(agenda):
        if e[0].lower() == nome_min:
            return p
    return None


def novo():
    global agenda, gravada
    agenda.append([pede_algo('Nome'), pede_algo('Telefone'),
                   pede_algo('Email'),     pede_algo('Data de nascimento')])
    gravada = False


def apaga():
    global agenda, gravada
    p = pesquisa_nome(pede_algo('Nome'))
    if p is not None:
        r = confirma(input('Tem certeza? [s/n] '))
        if r:
            gravada = False
            del agenda[p]
    else:
        print('Nome não encontrado.')


def altera():
    global agenda, gravada
    p = pesquisa_nome(pede_algo('Nome'))
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        email = agenda[p][2]
        datanasc = agenda[p][3]
        print('Encontrado: ')
        mostra_dados(nome, telefone, email, datanasc)
        r = confirma(input('Tem certeza? [s/n] '))
        if r:
            gravada = False
            agenda[p] = [pede_algo('Nome'), pede_algo('Telefone'),
                   pede_algo('Email'),     pede_algo('Data de nascimento')]
    else:
        print('Nome não ecnontrado.')


def lista():
    global agenda
    print('\nAGENDA\n----------\n')
    for i, e in enumerate(agenda):
        print(f'{i + 1}º Nome: {e[0]} | Telefone: {e[1]} | Email: {e[2]} | Nascimento: {e[3]}')
    print('----------\n')


def le(arq=None):
    global agenda, lida
    try:
        if not arq:
            arquivo = open(f'{pede_algo("Arquivo")}', 'r')
        else:
            arquivo = open(f'{arq}', 'r')
    except:
        print('Arqvuio inexistente.')
    else:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone, email, datanasc = linha.strip().split('#')
            agenda.append([nome, telefone, email, datanasc])
        arquivo.close()
        if agenda:
            lista()
            lida = True


def grava():
    global agenda, gravada
    arq_agenda = open('Agenda.txt', 'w')
    arquivo = open(f'{pede_algo("Arquivo")}.txt', 'w')
    for linha in agenda:
        arquivo.write(f'{linha[0]}#{linha[1]}#{linha[2]}#{linha[3]}\n')
        arq_agenda.write(f'{linha[0]}#{linha[1]}#{linha[2]}#{linha[3]}\n')
    arquivo.close()
    arq_agenda.close()
    gravada = True


def ordena():
    global agenda
    try:
        agenda.sort()
    except:
        print('Erro!')
    else:
        lista()


def menu():
    print(f'''
    Tamanho da agenda: {len(agenda)}  |  Status 
                            Gravada: {"Sim" if gravada else "Não"}
                            Lida: {"Sim" if lida else "Não"}

    1 - Novo               
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Ordenar

    0 - Sair
    ''')
    return int(input('Escolha uma opção: '))


