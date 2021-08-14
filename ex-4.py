
# NOTE: lists, tuples, and range objects are sequence types

# a função print possui um parâmetro chamado 'end'
# seu conteúdo default é um pula linha end='\n'
# se quisermos imprimir um número na frente do outro tem que mudar o parâmetro para vazio end=' '
# o tipo INT é um objeto não iterável por isso usamos range para saber o tamanho de 'numero'
# o uso de range faz com que não exista necessidade de incrementar o indice

numero = int(input('Digite um número\n'))

for index in range(numero):
    print('Estamos na posição:', index)
print('O número digitado foi', numero, 'a última posição do array foi', numero - 1, '\n')


# enumerate imprime o indice e o conteúdo

nome = 'andré'
for indice, letra in enumerate(nome):
    print('No indice', indice, 'temos a letra', letra)

for indice, letra in enumerate('andré'):
    print('No indice', indice, 'temos a letra', letra)
print()

nome = 'andré'
for x in nome:
    print(x, end='  ')
