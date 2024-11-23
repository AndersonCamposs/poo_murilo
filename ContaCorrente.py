class ContaCorrente:
    def __init__(self, nomeTitular, numeroConta, senha, saldo) -> None:
        self.nomeTitular = nomeTitular
        self.numeroConta = numeroConta
        self.senha = senha
        self.saldo = saldo
        

    def sacar(self, valorSaque):
        if(self.saldo >= valorSaque):
            self.saldo -= valorSaque
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def depositar(self, valorDeposito):
        self.saldo += valorDeposito
        print("Depósito realizado com sucesso")

    def aplicar(self, valorAplicacao): 
        if(self.saldo >= valorAplicacao):
            self.saldo -= valorAplicacao
            print("Aplicação realizada com sucesso")
            
        else:
            print("Saldo insuficiente")











