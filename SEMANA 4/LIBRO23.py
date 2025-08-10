"""Uso de cond. if"""

edad_1 = int(input("Ingrese la primera edad: "))
edad_2 = int(input("Ingrese la segunda edad: "))

if edad_1 > edad_2:
    print("La primera edad es mayor que la segunda.")
elif edad_1 == edad_2:
    print("Las edades ingresadas son iguales")
else:
    print("La segunda es mayor que la edad 1.")