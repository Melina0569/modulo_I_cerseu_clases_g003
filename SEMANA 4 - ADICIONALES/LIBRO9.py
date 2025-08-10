"""Usando propiedades de string"""

"""
Requisitos:
- Ingresar su nombre y apellido por consola
(varaibles distintas)
- Obtener el tamaño de tu nombre completo y muéstralo en consola
- Imprimir el resultado final, todo en mayusculas: .upper()
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
- Solamente ingresar el apellido paterno
"""

# Ingresar nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido paterno: ")

# Concatenar y calcular tamaño total
nombre_completo = nombre + " " + apellido
tamanio_nombre_completo = len(nombre_completo)

print("El tamaño de tu nombre completo es: {} caracteres".format(tamanio_nombre_completo))

print("En mayúsculas: ", nombre_completo.upper())

# Comparar tamaños
if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido.")
elif len(nombre) < len(apellido):
    print("El apellido es más largo que el nombre.")
else:
    print("El nombre y el apellido tienen el mismo tamaño.")
