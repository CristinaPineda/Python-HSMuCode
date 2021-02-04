"""
Nesse exemplo, há a simulação de uma calculadora básica com apenas quatro operações. 
A variável operacao é utilizada para determinar se será realizada a adição, subtração, divisão ou multiplicação.
Todo o código da função print() está indentado, indicando que a instrução pertence ao bloco.
O fim do bloco é marcado por um recuo na indentação.
"""

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um outro valor: '))
operacao = int(input('Digite o número da operação que deseja realizar: \
                        \n(1) - soma \
                        \n(2) - subtração \
                        \n(3) - multiplicação \
                        \n(4) - Divisão: \n'))

if (operacao == 1 ):
    print(valor1 + valor2)
if (operacao == 2 ):
    print(valor1 - valor2)
if (operacao == 3 ):
    print(valor1 * valor2)
if (operacao == 4 ):
    print(valor1 / valor2)