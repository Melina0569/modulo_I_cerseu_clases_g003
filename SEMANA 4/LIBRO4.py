"""Listas en Python"""

"""
Listas,
remove(): Elimina un elemento de la lista, indicando el valor
"""

var_1 = ["Python", "Javascript", "JAVA", "PHP", "Typescript"]

print("Mi lista tiene los siguientes valores: {}".format(var_1))

var_1.remove("PHP")
var_1.remove("JAVA")
print("Mi lista actualizada es: {}".format(var_1))

#Siempre debe imprimirse la lista, para que uno se pueda serciorar
#Para comprobar el metodo

print(var_1)