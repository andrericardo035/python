# Temperaturas em funções

def recebe_temperaturas():
    temperatura = []

    for i in range(10):
        temperatura.append(int(input('Digite uma temperatura: ')))
    return temperatura


def min_max():
    m = recebe_temperaturas()
    print(min(m))
    print(max(m))


if __name__ == '__main__':
    min_max()
