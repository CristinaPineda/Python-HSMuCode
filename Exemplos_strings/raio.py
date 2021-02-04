"""
Nesse exemplo, será criado um programa que pede o raio do círculo e calcula sua área.
A fórmula da área é A = π r², em que π (pí) é uma constante de valor aproximado 3,14.
O primeiro passo é criar um arquivo chamado area.py e definir a constante PI, de valor 3.14.
Por convenção, toda constante é definida com letras maiúsculas.
Em seguida, será pedido a entrada do usuário do tipo float e calculado a área.
Como o raio deve ser elevado ao quadrado, será utilizado o operador de potenciação **. 
Por último, o resultado será exibido em tela por meio da função print.
"""

PI = 3.14
raio = float(input('Digite o raio do círculo: '))
area = PI * (raio ** 2)
print(area)
