"""
Em programação, a recursão envolve problemas em que uma função chama a si mesma. 
Toda função recursiva possui uma condição base para que ela seja finalizada.

O que é recursão?
Recursão é um método de resolução de problemas que envolve quebrar um problema em subproblemas menores e menores até chegar a um problema pequeno o suficiente para que ele possa ser resolvido trivialmente. 
Normalmente recursão envolve uma função que chama a si mesma. 
Embora possa não parecer muito, a recursão nos permite escrever soluções elegantes para problemas que, de outra forma, podem ser muito difíceis de programar.

Ex: (panda.ime.usp.br)
Uma função iterativa que calcula a soma é mostrada no exemplo abaixo. A função usa uma variável acumuladora (theSum) para calcular o total de todos os números da lista iniciando com 0 e somando cada número da lista.
"""
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))

"""
Imagine por um minuto que você não tem laços while ou for. Como você calcularia a soma de uma lista de números? 
Em primeiro lugar, vamos reformular o problema soma em termos de listas de Python. 
Poderíamos dizer que a soma da lista numList é a soma do primeiro elemento da lista (numList [0]), com a soma dos números no resto da lista (numList [1:]). De forma funcional podemos escrever:

listSum(numList)=first(numList)+listSum(rest(numList))

Nesta equação first(numList) retorna o primeiro elemento da lista e rest(numList) retorna a lista com tudo menos o primeiro elemento.
"""
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))
