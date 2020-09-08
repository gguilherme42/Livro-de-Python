agenda = []


def pede_algo(palavra=''):
    resp = input(f'{palavra}: ')
    return resp if resp.find('#') else print(f'{palavra} inválida!')


def pesquisa_nome(nome):
    global agenda
    nome_min = nome.lower().strip()
    for p, e in enumerate(agenda):
        if e[0].lower() == nome_min:
            return p
    return None


def novo():
    global agenda
    nome = pede_algo('Nome')
    telefone = pede_algo('Telefone')
    agenda.append([nome, telefone])


def apaga():
    global agenda
    p = pesquisa_nome(pede_algo('Nome'))
    if p is not None:
        del agenda[p]
    else:
        print('Nome não encontrado.')


def altera():
    global agenda
    p = pesquisa_nome(pede_algo('Nome'))
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado: ')
        mostra_dados(nome, telefone)
        agenda[p] = [pede_algo('Nome'), pede_algo('Telefone')]
    else:
        print('Nome não ecnontrado.')


def lista():
    global agenda
    print('\nAGENDA\n----------\n')
    for i, e in enumerate(agenda):
        print(f'{i + 1}º Nome: {e[0]} | Telefone: {e[1]}')
    print('----------\n')


def le():
    global agenda
    try:
        arquivo = open(f'{pede_algo("Arquivo")}', 'r')
    except:
        print('Arqvuio inexistente.')
    else:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split('#')
            agenda.append([nome, telefone])
        arquivo.close()
        lista()


def grava():
    global agenda
    arquivo = open(f'{pede_algo("Arquivo")}', 'w')
    for linha in agenda:
        arquivo.write(f'{linha[0]}#{linha[1]}\n')
    arquivo.close()


def menu():
    print(f'''
    Tamanho da agenda: {len(agenda)}
    
    1 - Novo               
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    
    0 - Sair
    ''')
    return int(input('Escolha uma opção: '))


while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
