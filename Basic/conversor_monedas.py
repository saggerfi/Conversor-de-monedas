menu = """
Bienvenido al conversor de monedas 💴

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion =  int(input(menu))

if opcion == 1:
    dolares = float(input("Dólares USD: "))
    pesos = 3718.80
    resultado = dolares * pesos
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print("Tienes $" + resultado + "COL") 
elif opcion == 2:
    dolares = float(input("Dólares USD: "))
    pesos = 94.25
    resultado = dolares * pesos
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print("Tienes $" + resultado + "ARG") 
elif opcion == 3:
    dolares = float(input("Dólares USD: "))
    pesos = 19.87
    resultado = dolares * pesos
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print("Tienes $" + resultado + "MXN") 
else:
    print("Muy gracioso, ingresa una opción valida")

