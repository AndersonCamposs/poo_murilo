from ContaCorrente import ContaCorrente

class ContaPoupanca(ContaCorrente):
    def __init__(self, nomeTitular, numeroConta, senha, saldo, saldoPoupanca) -> None:
        super().__init__(nomeTitular, numeroConta, senha, saldo)
        self.saldoPoupanca = saldoPoupanca

    def resgatar(self, valorResgate):
        if(self.saldoPoupanca >= valorResgate):
            self.saldoPoupanca -= valorResgate
            self.saldo += valorResgate
            print("Resgate realizado com sucesso")
        else: 
            print("Saldo insuficiente")
