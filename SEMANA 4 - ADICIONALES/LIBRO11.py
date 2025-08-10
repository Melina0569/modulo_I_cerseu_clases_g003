"""Usando propiedades de string"""
"""Métodos String"""
"""Separación de strings: split()"""

cadena = "Python para la predicción de fraudes bancarios"

cadena_sin_espacios = cadena.split()

print("Nueva cadena: {}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)


cadena_sepracion_condicionada = cadena.split(sep="de")

print("Nueva cadena 2: {}".format(cadena_sepracion_condicionada))

for palabra in cadena_sepracion_condicionada:
    print(palabra)