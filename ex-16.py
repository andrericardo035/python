# Laço encadeado , tabuada

x = 1
y = 1

while x <= 10:
    print('Tabuada do:', x)
    while y <= 10:
        print(x, '*', y, '=', x * y)
        y += 1
    x += 1
    y = 1
print('Saiu do laço...')

# fazer com for tb
