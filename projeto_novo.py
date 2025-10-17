nomes = []
cpfs = []
contas = []
contador_de_contas = 1
LIMITE_EXTRATO = 3
extrato = 0
saques = 0

def filtrar_conta():
    if not nomes:
        print('Nenhuma conta cadastrada ainda!')
        return
    nome_busca = input('Quais dados por nome deseja buscar? ')
    encontrado = False
    for nome, cpf, conta in zip(nomes, cpfs, contas):
        if nome.lower() == nome_busca:
            print(f'✅ Conta encontrada!!!')
            print(f'Nome: {nome}')
            print(f'CPF: {cpf}')
            print(f'Conta: {conta}')
            encontrado = True
    if not encontrado:
        print(f'❌ Nenhuma conta encontrada!!!')
            


def saque():
    global extrato
    global saques
    if saques < LIMITE_EXTRATO:
        if extrato <= 0:
            print('Você não possui saldo para sacar.')
        else:
            valor_sacar = input('Valor a sacar: ')
            try:
                saques += 1
                valor_sacar = float(valor_sacar)
                print(f'Você sacou R${valor_sacar:.2f}')
                extrato -= valor_sacar
            except:
                saques -= 1
                print('Digite um número válido!')
    else:
        print('Você excedeu o limite de saques, tente novamente amanhã.')

def extrato_conta():
    print('#### EXTRATO DA CONTA ####')
    print()
    print()
    print()
    print(f'Saldo: {extrato:.2f}')


def deposito():
    global extrato
    valor = input('Valor a depositar: ')
    try:
        valor = float(valor)
        print(f'Você depositou R${valor:.2f}')
        extrato += valor
    except:
        print('Digite um número válido!')

def cadastrar_cliente():
    global contador_de_contas
    while True:
            nome = input('Digite seu nome: ')
            cpf = input('Digite seu cpf: ')
            nomes.append(nome)
            cpfs.append(cpf)
            numero_conta = str(contador_de_contas).zfill(4)
            contas.append(numero_conta)
            contador_de_contas += 1

            outra = input('Deseja criar outra conta? [S]im ou [N]ão?').lower().strip()
            if outra not in ('s', 'sim'):
                 break  
def listar_contas():
    if not nomes:
        print('Nenhuma conta foi criada ainda')
    else:
        print('\nNÚMERO DE CONTAS CADASTRADAS')
        for i in range(len(nomes)):
            print(f'{i+1}. {nomes[i]} | CPF: {cpfs[i]} | Conta: {contas[i]}')

def menu():
    while True:
        print('MENU INICIAL - ESCOLHA UMA OPÇÃO:')
        print()
        print(f'[0] Sair')
        print(f'[1] Listar conta')
        print(f'[2] Criar conta')
        print(f'[3] Sacar')
        print(f'[4] Depositar')
        print(f'[5] Extrato')
        print(f'[6] Filtrar conta')
        print()
        fazer = input('O que deseja fazer? ')
        if fazer == '0':
            print('Saindo do menu')
            break
        elif fazer == '1':
            listar_contas()
        elif fazer == '2':
            cadastrar_cliente()
        elif fazer == '3':
            saque()
        elif fazer == '4':
            deposito()
        elif fazer == '5':
            extrato_conta()
        elif fazer == '6':
            filtrar_conta()
        else:
            print('Selecione uma opção válida')

menu()