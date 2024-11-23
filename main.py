import random

import os

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

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
    elif(tipoConta == "2"):
        contaUsuario = ContaPoupanca(nomeTitular, numeroConta, senhaConta, depositoInicial, 0)
    else: 
        print("Você uma opção inválida no tipo de conta")

while(True):
    


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

        contaUsuario.sacar(valorSaque)

        print(f"Seu saldo atual é: {contaUsuario.saldo}")
        input("Pressione enter para continuar...")

    elif (acao == 2):
        print("Depósito")
    
    elif(acao == 0): 
        break
    else:
        print("AÇÃO INVÁLIDA, TENTE NOVAMENTE")
        input("Pressione enter para continuar...")



    os.system('cls')
