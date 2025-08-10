"""Listas en Python"""

"""
Listas, 
recorrido de las listas en un búcle for
"""

notas = [12, 11, 16, 19, 13]

i= 0
for nota in notas:
    print(nota)
    notas[i] = nota + 2
    i += 1

print(notas)