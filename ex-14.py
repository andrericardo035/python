# Aprendendo funções
# The correct mindset is to design your function to consume input from and only from its parameters in signature.

def soma(num1, num2):
    # jeito errado abaixo definindo a variável soma na função soma
    # soma = num1 + num2
    # return soma
    # pq se tiver uma variável soma definida globalmente e eu precisar mudar o nome dela...
    # ...ao dar 'replace all' vai mudar o nome aqui tb e pode interferir em como a função aqui é executada
    return num1 + num2


print('valor da soma é:', soma(10, 20))
print('valor da soma é:', soma(-10, 60))
print('valor da soma é:', soma(-10, -10))
