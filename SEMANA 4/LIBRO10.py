"""Listas en Python"""

"""
Listas,

del(): Eliminar un valor indicando un índice de la lista
"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Colombia")
paises.append("España")
paises.append("Canadá")
paises.append("México")

print("Mi lista de países: {}".format(paises))

del paises[2]

print("Mi lista actualizada: {}".format(paises))

del paises[4]

