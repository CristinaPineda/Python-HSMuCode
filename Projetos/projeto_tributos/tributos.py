#tributos

projeto_orcado = 56300
iss = 0.04
icms = 0.18

pagar_iss = projeto_orcado*iss
pagar_icms = projeto_orcado*icms

print(
	'O valor a ser pago para o projeto orçado da Empresa ZANPAX,\nlocalizada no estado de Pernambuco é de:\nISS: R$ {0:.2f}\nICMS: R$ {1:.2f}\nTOTAL DE IMPOSTOS: R$ {2:.2f}'.format(pagar_iss,pagar_icms,pagar_iss+pagar_icms))


