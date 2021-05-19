pesos = float(input("Pesos MXN: "))
equivalencia = 19.88
resultado = round(pesos / equivalencia, 2)
resultado = str(resultado)
print("Equivale a $" + resultado + "USD")
