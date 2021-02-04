
velocidade_aferida = int(input("Entre com a velocidade aferida: "))
limite_velocidade = int(input("Entre com a velocidade máxima da via: "))
placa = input("Entre com a placa do veículo: ")

velocidade_20 = limite_velocidade +(limite_velocidade * 0.20)
velocidade_50 = limite_velocidade +(limite_velocidade * 0.50)

infracao_media = "infração média (até '20%'acima do permitido da via)\n Multa de: R$ 130,16"
infracao_grave = "infração grave (de '21%' a '50%' acima do permitido da via)\n Multa de:R$ 195,23"
infracao_gravissima = "infração gravíssima ('51%'acima do permitido da via)\n Multa de:R$ 880,41"

cabecalho = "****PREFEITURA DA CIDADE DAS MULTAS****\n____AUTO DE INFRAÇÃO DE TRANSITO____\n"
msg = f"O veículo de placa {placa} passou no radar a velocidade de {velocidade_aferida}km/h em uma via de velocidade máxima permitida de {limite_velocidade}km/h."

if velocidade_aferida > limite_velocidade and velocidade_aferida <= velocidade_20:
	infracao = infracao_media
	multa = f"\nCometendo {infracao} "	
	print(cabecalho, msg, multa)
elif velocidade_aferida > velocidade_20 and velocidade_aferida <= velocidade_50:
	infracao = infracao_grave
	multa = f"\nCometendo {infracao} "	
	print(cabecalho, msg, multa)
elif velocidade_aferida > velocidade_50:
	infracao = infracao_gravissima
	multa = f"\nCometendo {infracao} "	
	print(cabecalho, msg, multa)








