# Tentativa de usar variáveis dinâmicas, exercício inacabado
# Usar variávis dinâmicas é uma péssima prática, era só para fins de estudo mesmo

for index in range(2):
    # variável dinnâmica
    globals()['matriz{}'.format(index)] = []
    print(globals())

    matriz = []
    n_linhas = int(input('\nDigite número de linhas da matriz: '))
    n_colunas = int(input('Digite número de colunas das matriz: '))

    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            valor = int(input('Digite o valor da posição [' + str(i) + ']' + '[' + str(j) + ']: '))
            linha.append(valor)
        matriz.append(linha)
    print(matriz)
    print('\n')
    globals()['matriz{}'.format(index)] = matriz

print(globals())
