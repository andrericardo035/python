# Coeficiente binomial utilizando funções
# Jeito pronto com funções python

import math

print(math.comb(10, 5))  # 252
print(math.comb(10, 10))  # 1
print(math.comb(55, 77))  # 1


# Na unha...
def fatorial(num):
    resultado = 1
    count = 1

    # O while pode incrementar ou decrementar <= para >=
    while count <= num:
        resultado *= count
        count += 1

    return resultado


def binomial(n, k):
    # n! / k! (n - k)!
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

# Nos inputs K tem que ser menor ou igual a N


if __name__ == '__main__':
    n1 = int(input('Digite um número para o cálculo binomial:\n'))
    n2 = int(input('Digite um número para o cálculo binomial:\n'))

    print('O binomial de:', n1, 'e', n2, 'é:', binomial(n1, n2))
