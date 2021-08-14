# Testes de controle de fluxo

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print('Não imprimiu o 3', i)
print('Saiu do while após executar tudo...')
print()

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('Não imprimiu o 5', var)
print('Saiu do while após executar tudo...')
print()

for i in range(10):
    if i == 3:
        continue
    print('Não imprimiu o 3', i)
print('Saiu do for após executar tudo...')
print()

# Lembre-se, python é fortemente ligada a identação
n = 0
while n < 10:
    print('imprimiu', n)
    n = n + 1  # identação correta
# n = n + 1  aqui identação errada causará loop infinito
print()

# range pode receber até 3 parâmetros, starts stop and step
for i in range(10):
    print(i)
print()

for i in range(7, 20):
    print(i)
print()

for i in range(5, 50, 5):
    print(i)
