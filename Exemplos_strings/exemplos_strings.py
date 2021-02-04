#
"""
E este programa deve imprimir apenas os caracteres de índice par por meio do fatiamento de strings. Será utilizado o str[::2], que indica uma cópia da string original, mas usando o passo 2. Dessa forma, ele fará a leitura a cada dois caracteres.
"""
# Imprimindo apenas os índices pares
str = 'Alemanha'

print(str[::2])


"""
Nesse segundo exemplo de strings, o programa deve retornar:

a frase fornecida com apenas a primeira letra em maiúsculo;

toda a frase em letras maiúsculas;

o comprimento total da frase.
"""
frase = 'um passo a frente e você não estará no mesmo lugar!'

# Método capitalize torna a primeira letra maiúscula
print(frase.capitalize())

# Método upper() retorna todos os caracteres em maiúsculo
print(frase.upper())

# Método len() retorna o comprimento da string
print('Tamanho da frase:', len(frase))


"""
Além da concatenação, é possível juntar strings por meio do método nativo join(), 
que une uma string por meio de um delimitador especificado.
Quando é necessário separar ou quebrar uma string, é possível utilizar o método split(), 
que irá separá-la conforme o delimitador indicado.
"""
# Usando a vírgula como delimitador juntamos as vogais
vogais = 'aeiou'
", ".join(vogais)
# a, e, i, o, u

# Quebrando a frase onde se tem uma vírgula
frase = 'Olá, mundo, incrível'
frase.split(', ')
# ['Olá', 'mundo', 'incrível']

"""
No último exemplo de strings, será dada uma lista com alguns super-heróis do universo em quadrinhos da Marvel.
A missão é escrever um programa que junte todos os heróis e os armazene em uma variável. 
Seus nomes devem ser delimitados por um hífen.
Após juntá-los na nova variável, eles devem ser separados onde estiver um espaço em branco. 
Confira o resultado no exemplo.
"""
marvel = ['Hulk', 'Thor', 'Iron Man', 'Captain America', 'Thanos', 'Black Panther']

herois = '-'.join(marvel)
# Hulk-Thor-Iron Man-Captain America-Thanos-Black Panther

herois.split(' ')
# ['Hulk-Thor-Iron', 'Man-Captain', 'America-Thanos-Black', 'Panther']