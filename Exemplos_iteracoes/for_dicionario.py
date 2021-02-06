"""
Esse exemplo consiste em um programa que vai informar o total gasto em compras realizadas em um shopping. 
Ele terá:

* uma variável total com valor igual a 0;

* um dicionário com todos os itens comprados e seus respectivos valores;

* o método values() para iterar apenas sobre os preços dos itens e adicioná-los à variável total;

* a exibição do valor total das compras.
"""
total = 0

compras = {
    "camisa": 79.99,
    "sapato": 299.99,
    "cinto": 50.00,
    "hamburguer": 22.80,
    "cinema": 35.50,
    "pipoca": 10.00,
    "estacionamento": 10.00
}

for item in compras.values():
    total = total + item

print("Total gasto R$ %.2f" % total)
