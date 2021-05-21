def main():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,    
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    # print(poblacion['Argentina'])
    # for pais in poblacion.keys():
    #     print(pais)
    # for pais in poblacion.values():
    #     print(pais)
    for pais, population in poblacion.items():
        print(f'{pais} tiene {population} habitantes')




if __name__ == '__main__':
    main()