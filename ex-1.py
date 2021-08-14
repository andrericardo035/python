# Conversão de temperaturas
# CUIDADO! A função input sempre devolve uma string

celsius = float(input('Digite a temperatura em graus celsius!\n'))

farenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print('A temperatura em farenheit é:', farenheit)
print('A temperatura em kelvin é:', kelvin)


# Cálculo do IMC

peso = 86
altura = 1.80

imc = peso / (altura ** 2)
print(imc)
print(f'O valor do imc é:{imc:.2f}')
