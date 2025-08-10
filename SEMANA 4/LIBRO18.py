"""Entrada y salida en Python"""

usuario = input('Usuario: ')
nombre = input('Nombre: ')
edad =  input('Edad: ')

print("Su usuario es: {}".format(usuario))
print("Bienvenido/a {}".format(nombre))

actualizar = int(edad) + 5
print("Actualización de edad: {}".format(actualizar))