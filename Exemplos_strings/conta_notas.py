"""
No exemplo quatro, será demonstrado o funcionamento de um caixa eletrônico bancário. 
O programa deve receber uma quantia e calcular o menor número de notas que totaliza um determinado valor.
As notas consideradas são 100, 50, 20, 10, 5, 2 e 1. 
No final, será informado quantas cédulas de cada valor são necessárias para retirar a quantia informada.
Por exemplo, R$491 necessita de quatro notas de R$100, uma de R$50, duas de R$20, uma de R$10 e uma de R$1.
"""

valor = int(input('Valor de saque R$: '))

cedulas_100 = int(valor / 100)
valor = valor % 100

cedulas_50 = int(valor/50)
valor = valor % 50

cedulas_20 = int(valor/20)
valor = valor % 20

cedulas_10 = int(valor/10)
valor = valor % 10

cedulas_5 = int(valor/5)
valor = valor % 5

cedulas_2 = int(valor/2)
valor = valor % 2

cedulas_1 = valor

print(
f'{cedulas_100} notas de R$100,00',
f'{cedulas_50} notas de R$50,00',
f'{cedulas_20} notas de R$20,00',
f'{cedulas_10} notas de R$10,00',
f'{cedulas_5} notas de R$5,00',
f'{cedulas_2} notas de R$2,00',
f'{cedulas_1} notas de R$1,00', sep='\n')