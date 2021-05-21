def conversor(tipo, pesos):
    dolares = float(input("Dólares USD: "))
    resultado = dolares * pesos
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print("Tienes $" + resultado + tipo)    


menu = """
Bienvenido al conversor de monedas 💴

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion =  int(input(menu))

if opcion == 1:
    conversor("COL", 3718.80)
elif opcion == 2:
    conversor("ARG", 94.25) 
elif opcion == 3:
    conversor("MXN", 19.87)
else:
    print("Muy gracioso, ingresa una opción valida")

