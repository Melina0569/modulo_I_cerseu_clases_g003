"""
Listas de Python - Participación
"""
"""
Requisitos:

- Crear dos listas vacías
- Asignar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de dos edades de ambas personas
- Sumar las listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
- Actualizar la profesion del segundo usuario
"""
lista_1 = []
lista_2 = []

print(lista_1)
print(lista_2)

lista_1.append("Melina")
lista_1.append(21)
lista_1.append("Investigación Operativa")

lista_2.append("Gaby")
lista_2.append(19)
lista_2.append("Estadística")

print("Lista 1: {}".format(lista_1))
print("Lista 2: {}".format(lista_2))

#la suma de las edades de las dos personas

suma_edades = lista_1[1] + lista_2[1]
print("La suma de las edades es: {}".format(suma_edades))

suma_listas = lista_1 + lista_2
print("La suma de las listas es: {}".format(suma_listas))

suma_listas.reverse()
print("Lista actualizada: {}".format(suma_listas))

suma_listas.pop(1)
suma_listas.pop(2)

print("Lista actualizada: {}".format(suma_listas))

#Actualizamos la profesion del segundo usuario
suma_listas[2] = "Matemática"

print("La lista actualizada queda así: {}".format(suma_listas))
"""
usuario[4] = 32
empleado[4] = 32
print(empleado)

"""



