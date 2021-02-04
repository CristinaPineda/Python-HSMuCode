"""
No terceiro exemplo, será calculada a média semestral de um aluno. 
O semestre é composto por três notas, cada uma com os pesos 2, 4 e 6, respectivamente.
Como primeiro passo, o programa deve solicitar a entrada das três notas. 
Em seguida, precisa calcular a média ponderada por causa dos pesos na composição das notas.
O resultado será armazenado na variável media e a saída será o valor da média com precisão de dois dígitos.
"""

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

media = ((nota1 * 2) + (nota2 * 4) + (nota3 * 6))/12
print(f'Média do semestre: {media:.2f}')