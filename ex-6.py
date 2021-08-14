# Imprime a posição e conteúdo da lista

colors = ["red", "green", "blue", "purple"]

print('lenght is', len(colors))
print('range is', range(len(colors)))

for index, content in enumerate(colors):
    print('The index is:', index, 'and the content is', content)
print()

# Imprime a posição somente
colors = ["red", "green", "blue", "purple"]

for index in range(len(colors)):
    print(index)
print()

# Imprime o conteúdo do índice

colors = ["red", "green", "blue", "purple"]

for index in range(len(colors)):
    print(colors[index])
print()
