"""Usando las propiedades de cadenas o strings"""

"""Concatenación"""

nombre = input("Nombre: ")
apellido = input("Apellido: ")

nombre_completo = nombre + " " + apellido
print("El nombre completo del usuario es: ", nombre_completo)

print("El nombre completo del usuario es: {} {}".format(nombre, apellido))