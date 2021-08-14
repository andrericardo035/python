# Diferentes maneiras de fazer concatenação em python

print()
print('Exercício: diferentes maneiras de fazer concatenação em python e imprimir na tela')

# a função print() por default já acrescenta new line ao ser executada
# logo... print('\n') pulará 2 linhas

print()
n1 = 5
n2 = 25

print('n1 = 5\nn2 = 25')
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 0')
print('print(\'A soma de n1 + n2 é\', n1 + n2)')
print('Saida: A soma de n1 + n2 é', n1 + n2)
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 1')
msg = 'teste'
print('msg = \'teste\'')
print('print(\'A soma de n1 + n2 é\', n1+n2, \'e este é um\', msg)')
print('Saida: A soma de n1 + n2 é', n1+n2, 'e este é um', msg)
print('--------------------------------------------------------------------------------')
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 2')
nome = 'André'
print('nome = \'André\'')
print('print(\'A soma de n1 + n2 é {} e meu nome é {}!\'.format(n1 + n2, nome))\'')
print('Saida: A soma de n1 + n2 é {} e meu nome é {}!'.format(n1 + n2, nome))
print('--------------------------------------------------------------------------------')
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 3')
nome = 'André Ricardo'
print('nome = \'André Ricardo\'')
print('print(\'A soma de n1 + n2 é\', str(n1 + n2) + \' e meu nome é\', nome + \'!\')')
print('Saida: A soma de n1 + n2 é', str(n1 + n2) + ' e meu nome é', nome + '!')
print('--------------------------------------------------------------------------------')
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 4')
nome = 'André Ricardo de Castro'
print('nome = \'André Ricardo de Castro\'')
print('print(f\'A soma de n1 + n2 é {n1 + n2} e meu nome é {nome}!\')')
print(f'Saida: A soma de n1 + n2 é {n1 + n2} e meu nome é {nome}!')
print('--------------------------------------------------------------------------------')
print()

print('--------------------------------------------------------------------------------')
print('#Modelo 5')
nome = 'André Ricardo de Castro dos Santos'
print('nome = \'André Ricardo de Castro dos Santos\'')
print('print(\'A soma de n1 + n2 é %d e meu nome é %s!\' %(n1+n2, nome))')
print('Saida: A soma de n1 + n2 é %d e meu nome é %s!' % (n1+n2, nome))
print('--------------------------------------------------------------------------------')
print()
