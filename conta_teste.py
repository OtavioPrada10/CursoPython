from conta import Conta
#Instanciação do objeto. (criando cliente)
conta = Conta('123-4','Lambarildo Peixe', 2000.00,1500.00)
conta.extrato()
conta.sacar(4000.00)
conta.extrato()

conta2 = Conta ('432-1','Tilapio Peixe',1600.00,1500.00)