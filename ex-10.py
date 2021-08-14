# Multiplicador de números digitados

produto = 1
contador = 0

while True:
    # Serão digitados quantos números o usuário quiser
    quantidade = int(input('Digite quantos números serão informados, ou 0 para sair:\n'))

    if quantidade == 0:
        break
    else:
        while contador < quantidade:
            valor = input('Digite um número:\n')
            if not valor.isdigit():
                print('Warning! Digito Inválido!')
            else:
                produto *= int(valor)
                contador += 1
        print('A multiplicação total foi:', produto)
        print('Programa finalizado!')

    # encerra o while true com break
    break
