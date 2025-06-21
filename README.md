# Desafio02 Digital Innovation One
Trilha Python. 

## Objetivos:
Modularizar o algoritmo de uma conta bancária com base em funções. A proposta é da plataforma Digital Innovation One como segundo desafio da trilha Python. Url do projeto original: [Conta bancário: DIO](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)

## Propostas da trilha Python:
* Separar as funcionalidades de saque, depósito e extrato em funções. Criar mais duas funções: cadastrar usuário e cadastrar conta bancária.
* Criar funções para todas as operações do sistema.
* A função saque deve receber os argumentos apenas por nome(keyword only).
* A função depósito deve receber os argumentos apenas por posição(positional only).
* A função extrato deve receber os argumentos por posição e nome(positional only e keyword only).
* O programa de armazenar os usuários em uma lista. O usuário é composto por nome, data de nascimento, cpf e endereço. Não podemos cadastrar dois usuários com o mesmo cpf.
* O programa deve armazenar as contas em uma lista. A conta é composta de: agência, número da costa e usuário.

## Modificações:
* Função ```Limpa_tela()``` através do módulo os.
* Entrada de dados com ```input()``` que somente aceitará números inteiros e de ponto flutuante, com ponto e vírgula, assim com o devido tratamento com ```try except```.
* Dicionário para as variáveis do sistema.
* Adição de ícones.

## Ferramentas utilizadas:
* Linguagem de programação Python 3.9.13
* Ambiente virtual VENV
* Git/GitHub
* Visual studio code
* Windows 10

## Modo de utilizar: 
* Clonar repositório.
* Acessar o diretório ```'cd desafio02-python-dio```.
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar a dependência, caso o projeto as tenha.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## Contribuição:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## Licença:
Este projeto é licenciado sob a Licença MIT.

## Comandos importantes
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.
