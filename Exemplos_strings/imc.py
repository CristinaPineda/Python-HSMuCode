"""
Nesse segundo exemplo, há um programa que calcula o Índice de Massa Corporal (IMC) de uma pessoa.
Inicialmente, ele pergunta o peso e a altura do indivíduo. A fórmula do IMC é IMC = peso/(altura)².
O resultado será exibido com a precisão de duas casas decimais.
Para variáveis do tipo float, quando for necessário determinar uma precisão das casas decimais, 
será utilizado a simbologia .2f, indicando que o desejado é dois dígitos decimais.
"""

altura = float(input('Informe sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso / (altura * altura)

print('Seu IMC é: %.2f' % imc)

"""
altura = float(input('Informe sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso / (altura * altura)

print(f'Seu IMC é: {imc}')
"""

