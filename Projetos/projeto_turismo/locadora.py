dias = 0
diaria = " "
carro = " "
escolha = " "
tipo_carro = 0
economico = 75.00
sedan = 110.00
suv = 180.00
com_opcional = True
opcao = " "
opciona = " "
seguro = 0.18

desconto = 0.15
taxa_adm = 75.00

def escolhendo():

  global tipo_carro; global economico; global sedan; global suv; global escolha; global diaria

  while (tipo_carro != 1 and tipo_carro != 2 and tipo_carro != 3):
    tipo_carro = int(input('''Escolha o tipo de carro que deseja alugar: 
        ( 1 ) ECONÔMICO
        ( 2 ) SEDAN
        ( 3 ) SUV\n'''))
    if tipo_carro == 1:
      diaria = economico
      escolha = " Econômico"
    elif tipo_carro == 2:
      diaria = sedan
      escolha = " Sedan"
    elif tipo_carro == 3:
      diaria = suv
      escolha = " SUV"

  print(f"O tipo de carro escolhido foi: {tipo_carro} -{escolha}.")
	
def diarias():
  global dias
  dias = int(input("Quantos dias deseja ficar com o carro? "))
  if dias < 7:
    promo = int(input("Aproveite nossa promoção! A partir de 7 dias de locação você recebe 15% de desconto na diaria! Deseja aproveitar? 1-SIM  2-NÃO"))
    if promo == 1:
      dias = int(input("Digite uma quantidade maior que 7 de dias deseja ficar com o carro? "))
    elif promo == 2:
      pass
  else:
    pass
  
  print(f"Dias de locação: {dias}")

def opcional():
  global com_opcional; global opcao; global opciona
  opcionais = int(input('''Deseja adicionar algum opcional? 
    Escolha:
    ( 1 ) GPS - R$ 12,00 por dia
    ( 2 ) Bebê Conforto - R$ 15,00 por dia
    ( 3 ) Cadeira de bebê -  R$ 15,00 por dia
    ( 4 ) Assento de Elevação - R$ 15,00 por dia
    ( 5 ) Sem opcional
    '''))
  gps = 12.00
  bebe_conforto = 15.00 
  cadeira_bebe = 15.00
  assento_elevacao = 15.00
  if opcionais == 5:
    com_opcional = False
    opciona = "Sem opcionais"
    print("Locação sem opcional escolhida!")
  elif opcionais == 4:
    com_opcional = True
    opcao = assento_elevacao
    opciona = "Assento de elevação"
    print("Opcional escolhido!")
  elif opcionais == 3:
    com_opcional = True
    opcao = cadeira_bebe
    opciona = "Cadeira de bebê"
    print("Opcional escolhido!")
  elif opcionais == 2:
    com_opcional = True
    opcao = bebe_conforto
    opciona = "Bebê conforto"
    print("Opcional escolhido!")
  elif opcionais == 1:
    com_opcional = True
    opcao = gps
    opciona = "Gps"
    print("Opcional escolhido!")

def total_locacao():
  global diaria; global dias; global taxa_adm; global com_opcional; global seguro_total
  global aluguel_opcional; global seguro_por_dia; global aluguel; global total_aluguel
  seguro_por_dia = (diaria * seguro)
  seguro_total = seguro_por_dia * dias
  aluguel = diaria * dias 

  if com_opcional:
    aluguel_opcional =  opcao * dias

    if dias >= 7:
      desconto = aluguel*0.15
      aluguel_descontado = aluguel - desconto
      total_aluguel = aluguel_descontado + seguro_total + aluguel_opcional + taxa_adm
    elif dias < 7:
      total_aluguel = aluguel + seguro_total + aluguel_opcional + taxa_adm

  else:
    aluguel_opcional = 0
    if dias >= 7:
      desconto = aluguel*0.15
      aluguel_descontado = aluguel - desconto
      total_aluguel = aluguel_descontado + seguro_total + taxa_adm
    elif dias < 7:
      total_aluguel = aluguel + seguro_total + taxa_adm
  print(f"O total do seu aluguel ficará em: R${total_aluguel}\nConfira abaixo o detalhamento das despesas\n\n")

def reciboLocacao():
  global escolha; global dias; global diaria; global aluguel; global seguro_por_dia; global seguro_total
  global seguro_total; global opciona; global opcao; global aluguel_opcional; global total_aluguel; global aluguel

  recibo = open('locacao.txt','w')
  recibo.write("ANDANDO BEM LOCADORA DE VEÍCULOS\n\n")
  recibo.write("Despesas de locação:\n")
  recibo.write(f"Tipo de carro: {escolha}\n")
  recibo.write(f"{dias} Diárias            Total\n")
  recibo.write(f"{dias} x R${diaria}           R${aluguel}\n")
  recibo.write("---------------------------------------------\n")
  recibo.write("Seguro do carro\n")
  recibo.write(f"{dias} x R${seguro_por_dia}      R${seguro_total}\n")
  recibo.write("---------------------------------------------\n")
  recibo.write(f"{opciona} - {dias} x R${opcao}     Total: R${aluguel_opcional}\n")
  recibo.write("---------------------------------------------\n")
  recibo.write("Taxa administrativa:    R$75.00\n\n")
  recibo.write(f"Total da locação: R${total_aluguel}" )

  recibo = open('locacao.txt', 'r')
  for linha in recibo:
    linha = linha.rstrip()
    print(linha)

def main():
  escolhendo()
  diarias()
  opcional()
  total_locacao()
  reciboLocacao()
main()