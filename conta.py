class Conta:
    #construtor
    def __init__(self,numero,titular,saldo,limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite              
        
    def extrato(self):
        print(f"Conta numero:{self.numero}`\
        Titular:{self.titular}\
        Saldo R$: {self.saldo}")
    #metodo depositar diheiro
    def depositar(self,valor):
        #self.saldo = self.saldo + valor
        self.saldo +=valor
        
        
    def sacar(self,valor):
        if(self.saldo < valor):
            print('Saldo insuficiente')
        else:
            self.saldo -=valor  
            print(f"Você sacou: {valor}")
    def transferencia_para(self,ebeficiario,valor):
        self.sacar(valor)
        beneficiario.depositar(valor)
        
        
        
        
        
        
        
        
        0,