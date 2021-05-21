def run():
    LIMITE = 1000000
    i = 0
    potencia_2 = 2**i 
    while potencia_2 < LIMITE:
        print(f'2 a la {i} es igual a {potencia_2}')
        i = i + 1
        potencia_2 = 2**i


if __name__ == '__main__':
    run()