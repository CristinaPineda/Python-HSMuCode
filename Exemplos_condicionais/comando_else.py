"""
O bloco do comando if apenas será executado se sua condição for testada como verdadeira. 
Se ela for falsa, o comando else será executado.

Nesse exemplo, o usuário digitará um número e o programa deve identificar se ele é par ou ímpar, exibindo uma mensagem com a informação.
Para que um número seja par, ele deve ser divisível por 2, ou seja, o resto da divisão será zero. Essa condição pode ser verificada por meio do operador módulo (%).
Caso o resto da divisão não seja zero, a condição if é testada como falsa e o bloco else será executado.
"""

numero = int(input('Digite um valor: '))

if numero % 2 == 0:
    print('{0} é um número par'.format(numero))
else:
    print('{0} é um número ímpar'.format(numero)
