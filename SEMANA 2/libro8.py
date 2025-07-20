"""
Requisitos:

1. Crear 4 variables, entre enteros, floats, booleans, string
2. Realizar el uso de condicionales de las variables para dos casos true y dos casos false
3. Para true: imprimir el valor de las otras dos variables
4. En dos condicionales, compararlo con un número

"""
var1 = 0
var2 = 21.5
var3 = False
var4 = "Perú"

if var3:
    print("Es correcto")
if var2:
    print("El país de origen es {}".format(var4))
if var4:
    print("{} {}".format(var1,var3))
if var2 < var1:
    print("Es verdadero")
