# tributos genericos, para ser usado com qualquer valor a ser inserido pelo usuário

nome_projeto = input("Qual o nome do seu projeto? ")
projeto_orcado = int(input("Digite o valor orçado do projeto: R$ "))
iss_input = input("Digite o valor do ISS cobrado em seu município (em porcentagem): ")
icms_input = input("Digite o valor do ICMS cobrado em seu estado (em porcentagem):  ")

iss = float(iss_input[:-1])/100
icms = float(icms_input[:-1])/100

pagar_iss = projeto_orcado*iss
pagar_icms = projeto_orcado*icms

print("O projeto ",nome_projeto,
 		" orçado em R$ ",
		projeto_orcado,"têm os seguintes valores de impostos a pagar: \nISS: R$ {0:.2f}\nICMS: R$ {1:.2f}\nTOTAL DE IMPOSTOS: R$ {2:.2f}".format(pagar_iss,pagar_icms,pagar_iss+pagar_icms))


