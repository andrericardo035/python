# Soma de matrizes usando lista de lista de lista, ainda inacabado

def create_matrice():
    matrice2 = []

    for index in range(1):
        matrice = []
        matrice.clear()
        line_numbers = int(input('\nMatrice number of lines: '))
        colunm_numbers = int(input('Matrice number of colunms: '))
        for i in range(line_numbers):
            line = []
            for j in range(colunm_numbers):
                value = int(input('Value position [' + str(i) + ']' + '[' + str(j) + ']: '))
                line.append(value)
            matrice.append(line)
        matrice2.append(matrice)

    print('\n')
    print(matrice2)
    # [ [[1, 2], [3, 4]], [[5, 6], [7, 8]] ]
    # c = []

    for i, valor in enumerate(matrice2):
        print('i', i, 'valor', valor)
        for an in i[0]:
            for en in i[1]:
                print(an, en)


if __name__ == '__main__':
    create_matrice()
