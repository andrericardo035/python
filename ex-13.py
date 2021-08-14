# Números adjascentes

print("Indicador de dois números adjacentes iguais...")
n = int(input("Digite um valor a ser testado: "))

y = False

while n != 0:
    a = n % 10
    # print('resto valor de a:', a)
    n = n // 10
    # print('novo valor inteiro de n:', n)
    b = n % 10
    # print('resto valor de b:', b)
    if a == b:
        print("O número", a, "possui dois digitos adjacentes iguais.")
        y = True

if y is not True:
    print("Não há números adjacentes iguais no valor digitado.")
