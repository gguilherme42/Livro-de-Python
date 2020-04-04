agenda = []
numerolista = []
# Novo contato
ncontato = 0
# Alteração
alterado = 0
# Exclusão
apagado = 0
# Lista gravada
lgravada = 0


def pergunta(msg='[s/n]', nome=''):
    # Obs: Um parâmetro opcional, nunca pode estar antes de um obrigatorio
    while True:
        try:
            p = str(input(msg)).strip().upper()[0]
        except (ValueError, TypeError):
            print(f'{cores("-> Erro! Digite S ou N.", 7)}')
        else:
            if p in 'SN':
                return p
            else:
                print(f'{cores("-> Erro! Digite S ou N", 7)}')


def pedenome(msg='Nome: ', o=False):
    global agenda
    while True:
        try:
            nome = str(input(msg)).strip()
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um nome válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            if o:
                # Se retornar None, o nome não foi cadastrado.
                if pesquisa(nome) is None:
                    return nome
                else:
                    print(f'{cores("Nome já cadastrado!", 7)}')
            else:
                return nome

def validaNumero(n):
    global numerolista
    for i, e in enumerate(numerolista):
        if e == n:
            return i
    return None


def pedenumero():
    global numerolista
    numerolista = []
    r = pergunta('Possui número de celular? [S/N]')
    if r == 'S':
        n = celular()
        numerolista.append(n)
    else:
        numerolista.append('')
    r = pergunta('Possui número de telefone? [S/N]')
    if r == 'S':
        n = telefone()
        numerolista.append(n)
    else:
        numerolista.append('')
    return numerolista


def celular(msg='Celular: '):
    while True:
        try:
            celular = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um número de celular válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            if pesquisaAgenda(celular) is None:
                return celular
            else:
                print(f'{cores("Celular já cadastrado!", 7)}')
                # O return quebra o laço


def telefone(msg='Telefone: '):
    while True:
        try:
            telefone = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um número de telefône válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            if pesquisaAgenda(telefone) is None:
                if validaNumero(telefone) is None:
                    return telefone
                else:
                    print(f'{cores("Telefone já cadastrado!", 7)}')
            else:
                print(f'{cores("Telefone já cadastrado!", 7)}')
                # O return quebra o laço


def pedeemail(msg='E-mail: '):
    global agenda
    while True:
        try:
            email = str(input(msg)).strip().lower()
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um email válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt as erro:
            print(f'-> Programa parado {erro}!')
            break
        else:
            # Se retornar None, o nome não foi cadastrado.
            if pesquisaemail(email) is None:
                return email
            else:
                print(f'{cores("E-mail já cadastrado!", 7)}')


def pedeaniversario(msg='Data de nascimento: '):
    from datetime import date
    while True:
        try:
            anv = str(input(msg)).strip()[:10]
        except Exception as erro:
            print(f'{cores(erro, 7)}')
        else:
            # Validação das barras de separação entre dia, mês e ano.
            if len(anv) == 10 and anv[2] == '/' == anv[5]:
                # 't' recebe o dia
                t = anv[0] + anv[1]
                d = int(t)
                # 't' recebe o mês
                t = anv[3] + anv[4]
                m = int(t)
                # 't' recebe o ano
                t = anv[6] + anv[7] + anv[8] + anv[9]
                a = int(t)
                if 0 < d <= 30 and 0 < m <= 12 and 1920 < a <= date.today().year:
                    return anv
                else:
                    print(f'{cores("Digite uma data válida!", 7)}')
            else:
                print(f'{cores("Digite:", 7)} {cores("dd/mm/aa", 4)}')


def mostradados(ind, nome, c, t, email='', aniversario=''):
    print(f'{ind}º Nome: {nome} | Celular: {c} | Telefone: {t}| E-mail: {email} | Aniversário: {aniversario}')


def pedenomeArquivo(msg='Nome do arquivo: '):
    while True:
        try:
            arq = str(input(msg))
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um nome válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            # O return quebra o laço
            return arq


def pesquisa(nome):
    mnome = nome.lower()
    for i, v in enumerate(agenda):
        t = v[0]
        if t.lower() == mnome:
            return i
    return None


# Pesquisa genéria para o número
def pesquisaAgenda(n):
    global agenda
    if len(agenda) >= 1:
        # v vai ser uma lista
        for v in agenda:
            # v[1] é onde estão os números
            numero = v[1]
            for i, e in enumerate(numero):
                if e == n:
                    return i
            return None


def pesquisaemail(email):
    memail = email
    for i, v in enumerate(agenda):
        if v[2] == memail:
            return i
    return None


def novo():
    global agenda, ncontato
    nome = pedenome('Nome: ', o=True)
    numero = pedenumero()
    email = pedeemail()
    aniversario = pedeaniversario()
    # Trata o nome, o telefone, email e o aniversário como elementos uma lista
    agenda.append([nome, numero, email, aniversario])
    ncontato += 1


def apaga():
    global agenda, apagado
    nome = pedenome()
    p = pesquisa(nome)
    if p is not None:
        print(f'Encontrado: {nome}')
        r = pergunta(f'Quer apagar o contato {nome}? [S/N]', nome)
        if r == 'S':
            print(f'-> Contato {nome} apagado!')
            del agenda[p]
        else:
            print(f'{cores("-> Exclusão negada!", 7)}')
    else:
        print(f'{cores("-> Nome não encontrado!", 7)}')
    apagado += 1


def altera():
    global alterado
    p = pesquisa(pedenome())
    if p is not None:
        nome = agenda[p][0]
        print(f'-> Encontrado: {nome}')
        r = pergunta(f'Quer alterar o contato {nome}? [S/N]', nome)
        if r == 'S':
            nome = pedenome()
            numero = pedenumero()
            email = pedeemail()
            aniversario = pedeaniversario()
            agenda[p] = [nome, numero, email, aniversario]
            print('-> Contato alterado!')
            print(f'Nome: {nome} | Celular: {numero[0]} | Telefone: {numero[1]} | E-mail: {email} | Aniversário: {aniversario}')
        else:
            print(f'-> Alteração Negada!')
    else:
        print(f'{cores("-> Nome não encontrado", 7)}')
    alterado += 1


def lista(ord=False):
    from time import sleep
    sleep(0.3)
    print('_' * 30)
    print('\nAgenda\n\n-----')
    sleep(0.1)
    if ord:
        for i, v in enumerate(sorted(agenda)):
            mostradados(i + 1, v[0], v[1][0], v[1][1], v[2], v[3])
        print('-----\n')
        print('_' * 30)
    else:
        for i, v in enumerate(agenda):
            mostradados(i + 1, v[0], v[1][0], v[1][1], v[2], v[3])
        print('-----\n')
        print('_' * 30)
    sleep(0.3)


def ler(normearq):
    global agenda, ncontato, apagado, alterado, lgravada
    agenda = []
    try:
        arquivo = open(f'{normearq}', 'r', encoding='utf-8')
        arquivoSalvo = open('salvo.txt', 'w', encoding='utf-8')
    except Exception as erro:
        print(f'{cores("Erro:", 7)} {erro}')
    else:
        for l in arquivo.readlines():
            nome, *n, email, aniversario = l.strip().split('#')
            arquivoSalvo.write(f'{nome}#{n[0]}#{n[1]}#{email}#{aniversario}\n')
            agenda.append([nome, n, email, aniversario])
        arquivo.close()
        arquivoSalvo.close()
        print(agenda)
        ncontato = apagado = alterado = 0


def grava():
    global agenda, ncontato, alterado, apagado, lgravada
    nomearquivo = pedenomeArquivo()
    try:
        arquivo = open(nomearquivo, 'w', encoding='utf-8')
    except Exception as erro:
        print(f'{cores("Erro!", 7)} {cores(erro, 7)}')
    else:
        for v in agenda:
            arquivo.write(f'{v[0]}#{v[1][0]}#{v[1][1]}#{v[2]}#{v[3]}\n')
        arquivo.close()
        ncontato = apagado = alterado = 0
        lgravada += 1
        ler(nomearquivo)


def validafaixa(perg='Escolha uma opção: ', inicio=0, fim=7):
    while True:
        try:
            valor = int(input(perg))
            if inicio <= valor <= fim:
                return valor
        except (ValueError, TypeError):
            print(f'Valor inválido! Digite entre {inicio} e {fim}')


c = ('\033[1;30;44m',  # 0  Fundo azul, letras brancas em negrito.
     '\033[1;30;43m',  # 1  Fundo amarelo, letras brancas em negrito.
     '\033[1;30;7m',   # 2  Fundo branco, letras pretas em negrito.
     '\033[m',         # 3  Fundo e letras padrão.
     '\033[1;30m',     # 4  Branco - negrito
     '\033[1;34m',     # 5  Azul - negrito
     '\033[1m',        # 6  Negrito
     '\033[1;31m'      # 7 Vermelho - Negrito
     )


def cores(f, cor=4):
    global c
    return f'{c[cor]}{f}{c[3]}'


def menu():
    from time import sleep
    global lgravada, ncontato, apagado, alterado
    sleep(0.5)
    print(f'''
{cores("-------------------------------------------------------", 6)}
{cores("1 - Novo")}            {cores("|", 6)}   {cores("* Lista atual:", 6)}                {cores("|", 6)}
{cores("2 - Altera")}          {cores("|", 6)}     - Contatos: {ncontato}               {cores("|", 6)}
{cores("3 - Apaga")}           {cores("|", 6)}     - Alterações da lista: {alterado}    {cores("|", 6)}
{cores("4 - Lista")}           {cores("|", 6)}     - Exclusões da lista: {apagado}     {cores("|", 6)}                                  
{cores("5 - Lista Ordenada")}  {cores("|", 6)}                                 {cores("|", 6)}      
{cores("6 - Grava")}           {cores("|", 6)}                                 {cores("|", 6)}
{cores("7 - Lê")}              {cores("|", 6)}   {cores("* Lista gravadas:", 6)} {lgravada}           {cores("|", 6)}                            
                    {cores("|", 6)}                                 {cores("|", 6)}     
{cores("0 - Sai", 5)}             {cores("|", 6)}                                 {cores("|", 6)} 
{cores("-------------------------------------------------------", 6)}
''', flush=True)
    sleep(0.25)
    return validafaixa()


def escreve(msg=''):
    from time import sleep
    global c
    sleep(0.25)
    print(f'{cores("=", 6)}'*30)
    print(f'{cores(msg, 5):^15}')
    print(f'{cores("=", 6)}'*30)
    sleep(0.25)

