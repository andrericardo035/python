# Fazer um programa que some o total dos números de um valor digitado
# Usando enumerate: Lembrando que enumerate não itera sobre números inteiros

numero = input('Digite um número bem grande:\n')

soma = 0

for index, character in enumerate(numero):
    soma += int(character)
print('A soma total dos números é:', soma)
print()

# Outra maneira de fazer é sempre pegando o resto da divisão por 10
# Usando while

n = int(input('Digite um número bem grande:\n'))
soma = 0

while n > 0:
    resto = n % 10
    soma = resto + soma
    n = n // 10
print('A soma total dos números é:', soma)
