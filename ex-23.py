# Cria, soma e imprime Matriz (teste) to mexendo nesse e o 20 é o original

def cria_matriz():
    dic_mat = {}

    for index in range(2):
        matriz = []
        print('Matriz', index + 1)
        n_linhas = int(input('\nDigite número de linhas: '))
        n_colunas = int(input('Digite número de colunas: '))
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                valor = int(input('Digite o valor da posição [' + str(i) + ']' + '[' + str(j) + ']: '))
                linha.append(valor)
            matriz.append(linha)
            dic_mat["matriz{}".format(index)] = matriz
        print()
    soma_matriz(dic_mat)


def soma_matriz(a):
    c = []

    for ind0, item0 in a.items():
        for ind1, item1 in a.items():
            if ind1 == 'matriz0':
                continue
            for lin in range(len(item0)):  # matriz0 [[1, 2], [3, 4]]
                for col in range(len(item0[0])):  # matriz1 [[5, 6], [7, 8]]
                    c.append(item0[lin][col] + item1[lin][col])
        break
    print('printou:', c)
    # para imprimir correto uma matriz 2x2 a lista teria que ser [ [1, 2], [3, 4] ]
    # mas por enquanto a lista contém [1, 2, 3, 4]


if __name__ == '__main__':
    cria_matriz()
