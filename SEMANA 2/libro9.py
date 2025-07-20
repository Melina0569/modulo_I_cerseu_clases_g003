"""
Reconocimiento de tipos de datos: type()
"""

#Creación de variables

nombre = "Luis"
ciudad = "Lima"
saldo = 5000
empresa = False
correo = "luishh@gmail.com"
empleado = [nombre, saldo, correo, ciudad, empresa]
empleado_4 = {'nomb':nombre,'ciud': ciudad, 'sald': saldo, 'corre': correo}

print("Tipo de dato de mi variable 'nombre' es {}".format(type(nombre)))
print("Tipo de dato de mi variable 'ciudad' es {}".format(type(ciudad)))
print("Tipo de dato de mi variable 'saldo' es {}".format(type(saldo)))
print("Tipo de dato de mi variable 'empresa' es {}".format(type(empresa)))
print("Tipo de dato de mi variable 'correo' es {}".format(type(correo)))
print("Tipo de dato de mi variable 'empleado' es {}".format(type(empleado)))
print("Tipo de dato de mi variable 'empleado_4' es {}".format(type(empleado_4)))


