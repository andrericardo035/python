# Manipulação de listas

dias_a_medir = 7
dia = 1
temperaturas = []

while dia <= dias_a_medir:
    temperaturas.append(int(input('Temperatura do dia ' + str(dia) + ': ')))
    dia += 1
print()
print('A lista de temperaturas é:', temperaturas)
print()
print('A minima temperatura foi:', min(temperaturas))

# -----------------------------------------------------------------------------
print()
lista_de_numeros = []

for i in range(3):
    lista_de_numeros.append(int(input("Digite um número: ")))
print('A lista é:', lista_de_numeros)

for i in lista_de_numeros:
    print(i, end=' ')

# -----------------------------------------------------------------------------
print()
print()
lista = []

for i in range(3):
    lista.append(str(input("Digite um numero:")))

print(lista)
print(' '.join(lista))
