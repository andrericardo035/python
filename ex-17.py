# Números primos

def primo(num):
    fator = 2
    if num == 2:
        return True
    while num % fator != 0 and fator <= num / 2:
        fator = fator + 1
    if num % fator == 0:
        return False
    else:
        return True


n = int(input('Digite um número inteiro e exibiremos os números '
              'primos até o número informado de forma decrescente:\n'))

while n > 1:
    # chama a função que verifica se o número é primo
    if primo(n):
        # se for imprime na tela
        print(n, end=' ')
    n -= 1

print('\n')

n = int(input('Digite um número inteiro e exibiremos os números '
              'primos até o número informado de forma crescente:\n'))
checar = 2

while checar < n:
    if primo(checar):
        print(checar, end=' ')
    checar += 1
