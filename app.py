import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    menu = f"""
    [1]\t DEPOSITAR
    [2]\t SACAR
    [3]\t EXTRATO
    [4]\t NOVA CONTA
    [5]\t LISTAR CONTAS
    [6]\t NOVO USUÁRIO
    [7]\t SAIR
    """

    print("=" * 42)
    print(" PYTHON ".center(42, "="))
    print("=" * 42)
    print(menu)
    print("=" * 42)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("\n🔍 INFORME O CPF (SOMENTE NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar_tela()
        print("\n❌ O CPF JÁ ESTÁ CADASTRADO!\n")
        return

    nome = input("🔍 INFORME SEU NOME COMPLETO: ")
    data_nascimento = input("🔍 INFORME A DATA DE NASCIMENTO (DD-MM-AAAA): ")
    endereco = input("🔍 INFORME O ENDEREÇO (LOGRADOURO, NÚMERO - BAIRRO - CIDADE/SIGLA DO ESTADO): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    limpar_tela()
    print("\n✅ USUÁRIO CRIADO COM SUCESSO!\n")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\n🔍 INFORME O CPF DO USUÁRIO: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar_tela()
        print("\n✅ CONTA CRIADA COM SUCESSO!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    limpar_tela()
    print("\n❌ USUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO DE CONTA ENCERRADO!\n")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"DEPÓSITO:\tR$ {valor:.2f}\n"
        limpar_tela()
        print("\n✅ DEPÓSITO REALIZADO COM SUCESSO!\n")
    else:
        print("\n❌ OPERAÇÃO FALHOU! O VALOR INFORMADO É INVÁLIDO.\n")

    return saldo, extrato    

def sacar(*, saldo, valor, extrato, valor_limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > valor_limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        limpar_tela()
        print("\n❌ OPERAÇÃO FALHOU! VOCÊ NÃO TEM SALDO SUFICIENTE.\n")

    elif excedeu_limite:
        limpar_tela()
        print("\n❌ OPERAÇÃO FALHOU! O VALOR DO SAQUE EXCEDE O LIMITE.\n")

    elif excedeu_saques:
        limpar_tela()
        print("\n❌ OPERAÇÃO FALHOU! NÚMERO MÁXIMO DE SAQUES EXCEDIDO.\n")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        limpar_tela()
        print("\n✅ SAQUE REALIZADO COM SUCESSO!\n")

    else:
        print("\n❌ OPERAÇÃO FALHOU! O VALOR INFORMADO É INVÁLIDO.")

    return saldo, extrato, numero_saques

def listar_contas(contas):
    limpar_tela()
    if contas:
        for conta in contas:
            print(" CONTAS ".center(42, "="))
            print("AGÊNCIA:\t", conta['agencia'])
            print("C/C:\t\t", conta['numero_conta'])
            print("TITULAR:\t", conta['usuario']['nome'].upper())
              
    else:
        limpar_tela()
        print("\n❌ NÃO EXISTE CONTA CADASTRADA.\n")    

def exibir_extrato(saldo, /, *, extrato):
    limpar_tela()
    print("\n================ EXTRATO ================")
    print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
    print(f"\nSALDO:\t\tR$ {saldo:.2f}")           
    
def principal():

    limpar_tela()

    dados = {
    "LIMITE_SAQUES": 3,
    "AGENCIA": "0001",   
    "saldo": 0,
    "limite": 500,
    "extrato": "",
    "numero_saques": 0,
    "usuarios": [],
    "contas": []
    }

    while True:
        menu()
        operacões = input("\n🔍 ESCOLHA UMA OPERAÇÃO => ")

        if operacões == "1":
            try:
                valor = float(input("\n🔍 INFORME O VALOR DO DEPÓSITO: "))

            except ValueError:
                limpar_tela()
                print("\n❌ OPERAÇÃO DE DEPÓSITO FALHOU! VALOR INVÁLIDO.\n")
                continue     

            dados["saldo"], dados["extrato"] = depositar(dados["saldo"], valor, dados["extrato"])

        elif operacões == "2":
            try:
                valor = float(input("\n🔍 INFORME O VALOR DO SAQUE: "))

            except ValueError:
                limpar_tela()
                print("\n❌ OPERAÇÃO DE SAQUE FALHOU! VALOR INVÁLIDO.\n")
                continue 

            dados["saldo"], dados["extrato"], dados["numero_saques"] = sacar(
                saldo = dados["saldo"],
                valor = valor,
                extrato = dados["extrato"],
                valor_limite = dados["limite"],
                numero_saques = dados["numero_saques"],
                limite_saques = dados["LIMITE_SAQUES"],
            )

        elif operacões == "3":
            exibir_extrato(dados["saldo"], extrato=dados["extrato"])

        elif operacões == "4":
            numero_conta = len(dados["contas"]) + 1
            conta = criar_conta(dados["AGENCIA"], numero_conta, dados["usuarios"])

            if conta:
                dados["contas"].append(conta)

        elif operacões == "5":
            listar_contas(dados["contas"])

        elif operacões == "6":
            criar_usuario(dados["usuarios"])

        elif operacões == "7":
            limpar_tela()
            print(f"\nOBRIGADO. ATÉ A PRÓXIMA!\n")
            break
        else:
            limpar_tela()
            print("\n❌ OPERAÇÃO INVÁLIDA, SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.\n")

principal()