"""
Listas en Python

Listas len()
Se obtiene el tamaño de la lista en Python
append(): Agrega elementos
"""
paises = []    #inicio una lista vacía

print("Mi lista de paises, tiene los siguientes elementos: {}".format(paises))
print("Tamaño de mi lista: {}".format(len(paises)))

"""Agregar datos a la lista"""

paises.append("Perú")
paises.append("España")
paises.append("Colombia")

print("Mi lista actualizada de paises, tiene los siguientes elementos: {}".format(paises))
print("Tamaño de mi lista: {}".format(len(paises)))

paises.append("Argentina")
print("Mi nueva lista actualizada de paises: {}".format(paises))

#Usar específicamente un elemento de mi lista
pais = paises[0]
print("El primer elemento (0) de mi lista es: {}".format(pais))
