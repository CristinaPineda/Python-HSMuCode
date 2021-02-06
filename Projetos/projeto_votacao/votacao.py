apt = []
voto = ""
candidato_azul = 0
candidato_vermelho = 0
candidato_amarelo = 0
brancos_e_nulos = 0

apartamentos = 0

while apartamentos < 35: 
	print("SISTEMA DE VOTAÇÃO ELETRÔNICA DO CONDOMINIO 'Aqui todo mundo é legal'\n 		¨¨¨¨¨¨ELEIÇÃO SINDICAL¨¨¨¨¨¨")
	ap = int(input("Informe o número do seu apartamento: "))
	if ap in apt:
		print("O apartamento informado já computou o voto e não pode votar novamente")
	else:
		apt.append(ap)
		voto = input("Digite o seu voto:\nDigite 1 para CANDITADO CHAPA AZUL\nDigite 2 para CANDITADO CHAPA VERMELHA\nDigite 3 para CANDITADO CHAPA AMARELA\nDigite BRANCO para votar em branco e NULO para anular seu voto\n")
		if voto == "1":
			candidato_azul += 1
			print('Voto computado com sucesso!\n***FIM***\n')
		elif voto == "2":	
			candidato_vermelho += 1
			print('Voto computado com sucesso!\n***FIM***\n')
		elif voto == "3":
			candidato_amarelo += 1
			print('Voto computado com sucesso!\n***FIM***\n')
		else:
			brancos_e_nulos = brancos_e_nulos + 1
			print('Voto computado com sucesso!\n***FIM***\n')
		apartamentos += 1
		votos_validos = candidato_azul+candidato_amarelo+candidato_vermelho

print(apt)
print(f"Apuração dos votos: Candidato chapa azul: {candidato_azul} votos\nCandidato chapa vermelha: {candidato_vermelho} votos\nCandidato chapa amarela: {candidato_amarelo} votos\nVotos brancos e nulos {brancos_e_nulos}.")
print(f"A chapa azul obteve'", (candidato_azul/votos_validos)*100, "%' dos votos válidos.")
print(f"A chapa vermelha obteve'", (candidato_vermelho/votos_validos)*100, "%' dos votos válidos.")
print(f"A chapa amarela obteve'", (candidato_amarelo/votos_validos)*100, "%' dos votos válidos.")



#Cristina Pineda