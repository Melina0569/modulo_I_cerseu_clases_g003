"""
Conversión de datos
"""

#Creación de variables

var_str = "54796" #54796 -> en este caso no lo podrá convertir
nombre = "Johanna"
modulo = 2
prom = 18.9

# Conversión de string a entero

var_int = int(var_str)
print(var_int)

# Conversión de entero a string
var_mod = str(modulo)
print(var_mod)
print (type(var_mod))

# Conversión de string a entero (no será)
#var_nom = int(nombre)
#print(type(var_nom))

#Conversión de flotante a entero
var_int = int (prom)
print(var_int)
print(type(var_int))