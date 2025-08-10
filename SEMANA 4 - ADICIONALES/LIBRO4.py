"""Uso del bucle while"""

"""Utilizando: break"""

numero = 1

while True:
    print("numero: ", numero)
    numero += 1

    if numero > 10:
        print("Esto detendrá al bucle")
        break  #Detiene el bucle