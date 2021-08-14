# Cria e imprime Matriz

def le_matriz():
    n_linhas = int(input('Digite número de linhas da matriz: '))
    n_colunas = int(input('Digite número de colunas das matriz: '))
    cria_matriz(n_linhas, n_colunas)


def cria_matriz(linhas, colunas):

    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input('Digite o valor da posição [' + str(i) + ']' + '[' + str(j) + ']: '))
            linha.append(valor)
        matriz.append(linha)

    # Aqui já saiu do for principal
    print(matriz)
    imprime_matriz(matriz)


def imprime_matriz(a):
    print('Imprimindo a lista em forma de matriz...')
    for i in a:
        print(i)

    print('Imprimindo cada indice e o seu conteúdo...')
    for i in enumerate(a):
        print(i)


if __name__ == '__main__':
    le_matriz()
