"""Listas en Python"""

"""
Listas,

copy(): Obtener todos los elementos de una lista a otra nueva lista
"""

var_1 = ["SqLServer", "rDS", "MYSQL", "PostgreSQL", "MariaDB"]

#Lista clon

var_2 = var_1.copy()

print("Elementos de mi nueva lista: {}".format(var_2))

var_2.append("SQLite3")
print("Mi lista actualizada: {}".format(var_2))

print("Lista original: {}".format(var_1))