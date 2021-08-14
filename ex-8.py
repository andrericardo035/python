# Menor nome em ordem alfabética

def menor_nome(nome):
    nova_lista = []

    for index in nome:
        r = index.strip()
        r = r.capitalize()
        nova_lista.append(r)
    print(nova_lista)
    print('O menor nome em ordem alfabética é: ', min(nova_lista))


if __name__ == '__main__':
    nomes = []

    for i in range(4):
        nomes.append(input('Digite o nome de alguém: '))
    menor_nome(nomes)
