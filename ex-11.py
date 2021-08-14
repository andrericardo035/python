# Equação do segundo grau ex: x² - 6x + 5 = 0
# Valores de entrada para o programa serão a, b e c

import math

a = int(input('Digite o número A\n'))
b = int(input('Digite o número B\n'))
c = int(input('Digite o número C\n'))

delta = b ** 2 - 4 * a * c
print('O valor de delta é', delta)

if delta < 0:
    print('Esta equação não possui valores reais')
elif delta == 0:
    x = (-b) / (2 * a)
    print('O valor de x1 é', x)
    print('O valor de x2 é', x)
else:
    # usando math.sqrt para calcular a raiz quadrada
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    # elevar a 'meio' é um jeito de obter a raiz quadrada
    # x1 = (-b + delta ** (1/2)) / (2 * a)
    # x2 = (-b - delta ** (1/2)) / (2 * a)
    print('O valor de x1 é', x1)
    print('O valor de x2 é', x2)
