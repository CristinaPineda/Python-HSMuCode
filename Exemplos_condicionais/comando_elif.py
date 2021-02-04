"""
O comando elif é útil quando há mais de uma condição a ser testada. 
O resultado que ele produz também pode ser obtido utilizando vários comandos if's aninhados.
Porém, assim que o número de condições aumentar, a leitura do programa ficará mais difícil.

No exemplo ao lado, o programa deve retornar o nome da capital de alguns estados do Brasil. 
Caso o usuário informe um estado que não consta na lista, ele deve ser informado que o estado não foi cadastrado.
Há várias condições que serão testadas por meio do comando elif.
"""
estado = input('Nome de um estado: ').lower()

if 'ceara' in estado:
    print('Fortaleza')
elif 'bahia' in estado:
    print('Salvador')
elif 'minas gerais' in estado:
    print('Belo Horizonte')
elif 'amazonas' in estado:
    print('Manaus')
else:
    print('O estado inserido ainda não foi cadastrado!')
