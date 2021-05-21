import random


def main():
    numero_ganador = random.randint(1, 100)
    numero = int(input('Escoge un numero: '))
    while numero != numero_ganador:
        if numero > numero_ganador:
            print('Busca un número menor')
        else:
            print('Busca un número mayor')
        numero = int(input('Escoge otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    main()