import random

import os

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

def verificarSenha(senhaBase, senhaVerificacao) -> bool: 
    return (senhaBase == senhaVerificacao)
while (True):
    tipoConta = input("Informe o tipo da conta (1 - CORRENTE, 2 - POUPANÇA): ")
    nomeTitular = input("Informe o seu nome: ")
    digitoUm = str(random.randint(0, 9))
    digitoDois = str(random.randint(0, 9))
    digitoTres = str(random.randint(0, 9))
    numeroConta = digitoUm + digitoDois + digitoTres

    senhaConta = input("Informe a senha da sua conta: ")

    depositoInicial = float(input("Informe o valor do seu depósito inicial: "))

    if (depositoInicial < 10): 
        print("O depósito inicial deve ser de, no mínimo, R$ 10,00.")
    else :
        if (tipoConta == "1"):
            contaUsuario = ContaCorrente(nomeTitular, numeroConta, senhaConta, depositoInicial)
            break
        elif(tipoConta == "2"):
            contaUsuario = ContaPoupanca(nomeTitular, numeroConta, senhaConta, depositoInicial, 0)
            break
        else: 
            print("Você escolheu uma opção inválida no tipo de conta, tente criar sua conta novamente.")
        
        input("Pressione enter para continuar...")
        os.system("cls")


tentativas = 3
while(True):

    #VERIFICA SE O USUÁRIO AINDA TEM TENTATIVAS 
    if (tentativas == 0):
        print("Você errou a senha três vezes, sua conta foi bloqueada.")
        input("Pressione enter para continuar...")

        break

    print('''
    INFORME A SUA AÇÃO:
        0 - SAIR
        1 - SACAR
        2 - DEPOSITAR
        3 - APLICAR
        4 - RESGATAR
''')
    acao = int(input())

    if (acao == 1): 
        valorSaque = float(input("Informe o valor do saque: "))
        senhaDigitada = input("Digite a sua senha: ")
        
        # VERIFICA SE A SENHA DO USUÁRIO É CORRETA, SE NÃO FOR, CAI NO ELSE DA LINHA 67
        if (verificarSenha(contaUsuario.senha, senhaDigitada)):
            contaUsuario.sacar(valorSaque)

            print(f"Seu saldo atual é: {contaUsuario.saldo}")
        else:
            tentativas-=1
            print(f"Senha errada, você tem mais {tentativas} tentativas")

        input("Pressione enter para continuar...")

        

    elif (acao == 2):
        print("Depósito")

    elif (acao == 3):
        valorAplicacao = float(input("Informe o valor a ser aplicado: "))
        senhaDigitada = input("Digite a sua senha: ")
        if (verificarSenha(contaUsuario.senha, senhaDigitada)):
            valorAplicado = contaUsuario.aplicar(valorAplicacao)
            contaUsuario.saldoPoupanca += valorAplicado

        else:
            tentativas-=1
            print(f"Senha errada, você tem mais {tentativas} tentativas")

        input("Pressione enter para continuar...")


    
    elif(acao == 0): 
        break
    else:
        print("AÇÃO INVÁLIDA, TENTE NOVAMENTE")
        input("Pressione enter para continuar...")



    os.system('cls')
