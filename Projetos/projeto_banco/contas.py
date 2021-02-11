import random

class Cliente:
	def __init__(self, titular):
		self.titular = titular


class ContaComum(Cliente):
	def __init__(self, agencia, titular, rendaMensal):
		super().__init__(titular)
		Cliente.__init__(self, titular)
		self.agencia = agencia
		self.numero_conta = random.randrange(0,9999) #primeiro número do range incluso e o último não incluso
		self.digito = random.randrange(0,10)
		self.rendaMensal = rendaMensal
		self.saldo = 0
		self.limite = random.randrange(rendaMensal, (rendaMensal*2))

	def exibeCliente(self):
		print("Nome do titular da conta:",self.titular, "\n", self.agencia, "Agência\n", self.numero_conta, "-", self.digito, "Conta e digito\n", "Saldo atual: R$", self.saldo)

	def deposito(self, valor_deposito):
		self.saldo = self.saldo + valor_deposito
		print(f"Valor depositado: R${valor_deposito}.")

	def consultaSaldo(self):
		print(f"Saldo atual em conta: R${self.saldo}.")

	def saque(self, valor_saque):
		taxa = 0.0199  #1,99% por saque
		taxaSaque = round(valor_saque * taxa, 2) 
		if valor_saque < (self.saldo):
			self.saldo -= valor_saque 
			print(f"Valor do saque: RS{valor_saque}.\nSaque aprovado, aguarde a contagem das cédulas.")
		elif (valor_saque > self.saldo) and (valor_saque <= (self.saldo + self.limite + taxaSaque)):
			self.saldo -= valor_saque
			print(f"Valor do saque: R${valor_saque}.\nSaque aprovado com o uso do limite especial, aguarde a contagem das cédulas.")
		else:
			print("Saldo insuficiente")


#instanciar clientes


cliente1 = ContaComum(1234, "Fulano de tal", 1200)
cliente1.exibeCliente()
cliente1.deposito(3000)
cliente1.consultaSaldo()
cliente1.deposito(4000)
cliente1.consultaSaldo()
cliente1.saque(3100)


#Cristina Pineda 