numero = 0

while numero < 20:
    print('A potencia de', numero, 'para dois é:', 2 ** numero)
    numero += 1
print()

# Ao digitar 0 o programa irá parar a execução e mostrar o valor dos números digitados

soma = 0

while True:
    # Serão digitados quantos números o usuário quiser
    valor = input('Digite um número para somar ou 0 para sair:\n')
    if not valor.isdigit():
        print('Warning! Digito Inválido!')
    elif valor.isdigit() and valor != '0':
        soma += int(valor)
        print('Você digitou', valor)
        print('A soma atual é', soma)
    else:
        print('A soma total é:', soma)
        print('Programa finalizado!!')
        break
