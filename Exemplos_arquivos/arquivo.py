"""
ABRINDO UM ARQUIVO DE TEXTO EM PYTHON 

A leitura de um arquivo em Python é realizada por meio da função nativa open(), que recebe como parâmetro o nome do arquivo ou, de forma opcional, sua localização completa.
"""

file = open("teste.txt")

# Endereço completo do arquivo
file = open("/Documentos/PastaPessoal/CursoPython/teste.txt")

"""
Na função open(), é necessário especificar o modo da operação que será realizada no arquivo. Por exemplo, r é indicado para leitura, w para escrita e b para arquivos binários.

Por padrão, se ele não for indicado, o modo leitura será considerado. Confira na próxima página a tabela com todos os modos disponíveis.
"""

file = open("teste.txt", 'r') # modo de leitura
file = open("teste.txt", 'w' ) # modo de escrita


#Após realizar a leitura de um arquivo, ele sempre deve ser fechado. Para isso, será utilizada a função close(), 
#assegurando que não ocorra nenhuma mudança ou evitando que o arquivo seja corrompido de alguma maneira.


# Abrindo um arquivo
file = open("teste.txt", "w" )

print("Nome do arquivo: ", file.name)

# Fechando o arquivo
file.close()

"""
ESCREVENDO UM ARQUIVO DE TEXTO EM PYTHON 

Para criar um programa que manipula uma lista de compras, primeiramente crie um arquivo chamado produtos.py, 
por meio do seu editor de texto.
Em seguida, utilize a função open() para criar um arquivo compras.txt em modo w. 
Lembre que se esse arquivo já existisse, o modo 'w' iria apagar todo o conteúdo. Como ele não existe ainda um novo arquivo será criado.
Utilizando o método .write(), escreva alguns itens da lista de compras. 
Por fim, feche o arquivo. Ao executar o programa, note que o compras.txt foi criado no mesmo diretório do produtos.py.
"""

file = open("compras.txt", "w")

file.write('Água\n')
file.write('Arroz\n')
file.write('Detergente\n')

file.close()

#O read() é uma das maneiras que o Python oferece para ler um arquivo. Nesse caso, o método retorna todo o texto contido no compras.txt.

file = open("compras.txt", "r")

# Faz a leitura de todo o conteúdo do txt
print(file.read())

file.close()

#LEITURA DE UM ARQUIVO DE TEXTO EM PYTHON 

"""
Há outras maneiras de realizar a leitura do conteúdo de um arquivo sem ser por inteiro.
O método readline() faz a leitura de apenas uma linha e o readlines() retorna uma lista contendo todas as linhas.
A lista que o método readlines() retorna contém \n no final de cada elemento, indicando que houve uma quebra de linha. 
Dessa forma, o interpretador sabe que deverá realizar a leitura da próxima.
"""
file = open("compras.txt", "r")

# Retorna a primeira linha do txt
print(file.readline())
# Água

# Retorna a segunda linha do txt
print(file.readline())
# Arroz

print(file.readlines())
# ['Água\n', 'Arroz\n', 'Detergente']

file.close()

#Caso seja necessário adicionar mais itens no arquivo compras.txt, todo o conteúdo anterior será apagado. Para solucionar esse problema, é só alterar o modo em que o arquivo será aberto, saindo do w para o a, que irá preservar o conteúdo já existente.

file = open("compras.txt", "a")

file.write('Bolacha\n')
file.write('Peixe\n')
file.write('Ovos\n')

file.close()

