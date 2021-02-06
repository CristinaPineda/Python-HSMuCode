"""
O exemplo 2 busca remover todas as ocorrências do número 20.
Por meio do comando if, é possível verificar quando um número é igual ou não a 20. 
Dessa forma, ele será removido sempre que for encontrado. 
Caso contrário, o programa segue com sua execução até ter percorrido todos os itens da lista.


lista1 = [5, 20, 15, 20, 25, 50, 20]

for num in lista1:
    if num == 20:
        lista1.remove(num)

print(lista1)
"""
estados = {"bahia": "salvador", "amazonas":"manaus","parana":"curitiba", "alagoas":"maceio"}
while len(estados) > 4:

	print(estados.popitem())
	
print("Loop finalizado")