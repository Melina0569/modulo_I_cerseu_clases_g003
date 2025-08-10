"""Listas en Python"""

"""
Listas,

count(): Cantidad de veces que se repite un elemento dentro de la lista
"""

var_1 = ["Python", "Javascript", "JAVA", "PHP", "Typescript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("NodeJS")

print("Lista actualizada: {}".format(var_1))

print("Cantidad de veces que se repite 'Python': {}".format(var_1.count("Python")))
print("Cantidad de veces que se repite 'JAVA': {}".format(var_1.count("JAVA")))
