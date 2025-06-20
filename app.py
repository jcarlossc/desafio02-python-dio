import os

# Função para limpar tela.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função menu.
def menu():
    cabecalho = "=" * 42
    titulo = " PYTHON ".center(42, "=")
    rodape = "=" * 42
    menu = f"""
    {cabecalho}
    {titulo}
    {cabecalho}
    [1]\t DEPOSITAR
    [2]\t SACAR
    [3]\t EXTRATO
    [4]\t NOVA CONTA
    [5]\t LISTAR CONTAS
    [6]\t NOVO USUÁRIO
    [7]\t SAIR
    {rodape}
    ESCOLHA UMA OPERAÇÃO => """
    return input(menu)
    
menu()