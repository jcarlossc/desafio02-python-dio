import os

# Função para limpar tela.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função menu.
def menu():
    # Variáveis de design.
    linhas = "=" * 42
    titulo = " PYTHON ".center(42, "=")
    # Variável do menu.
    menu = f"""
    {linhas}
    {titulo}
    {linhas}
    [1]\t DEPOSITAR
    [2]\t SACAR
    [3]\t EXTRATO
    [4]\t NOVA CONTA
    [5]\t LISTAR CONTAS
    [6]\t NOVO USUÁRIO
    [7]\t SAIR
    {linhas}
    ESCOLHA UMA OPERAÇÃO => """

    return input(menu)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("\n🔍 INFORME O CPF (SOMENTE NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar_tela()
        print("❌ O CPF JÁ ESTÁ CADASTRADO!")
        return

    nome = input("🔍 INFORME SEU NOME COMPLETO: ")
    data_nascimento = input("🔍 INFORME A DATA DE NASCIMENTO (DD-MM-AAAA): ")
    endereco = input("🔍 INFORME O ENDEREÇO (LOGRADOURO, NÚMERO - BAIRRO - CIDADE/SIGLA DO ESTADO): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    limpar_tela()
    print("✅ USUÁRIO CRIADO COM SUCESSO!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\n🔍 INFORME O CPF DO USUÁRIO: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar_tela()
        print("\n✅ CONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    limpar_tela()
    print("\n❌ USUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO DE CONTA ENCERRADO!")
    
def principal():

    limpar_tela()
    # Dicionário de variáveis e listas do sistemas.
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

    # Estrutura que centraliza o sistema.
    while True:

        operacões = menu()

        if operacões == "1":
            pass
        elif operacões == "2":
            pass
        elif operacões == "3":
            pass
        elif operacões == "4":
            numero_conta = len(dados["contas"]) + 1
            conta = criar_conta(dados["AGENCIA"], numero_conta, dados["usuarios"])

            if conta:
                dados["contas"].append(conta)

        elif operacões == "5":
            pass
        elif operacões == "6":
            criar_usuario(dados["usuarios"])

        elif operacões == "7":
            limpar_tela()
            print(f"\nOBRIGADO, {dados["usuarios"][0]["nome"].upper()}. ATÉ A PRÓXIMA!\n")
            break
        else:
            limpar_tela()
            print("❌ OPERAÇÃO INVÁLIDA, SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.")

principal()