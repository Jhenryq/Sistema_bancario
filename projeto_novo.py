nomes = []
cpfs = []
contas = []
contador_de_contas = 1
def cadastrar_cliente():
    global contador_de_contas
    while True:
        # resposta = input('Deseja criar uma conta? ').lower()
        # if resposta == 's' or resposta == 'sim':
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
            
        # else:
        #     print('Saindo do programa')
        #     break   
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
        print()
        fazer = input('O que deseja fazer? ')
        if fazer == '0':
            print('Saindo do menu')
            break
        elif fazer == '1':
            listar_contas()
        elif fazer == '2':
            cadastrar_cliente()

menu()