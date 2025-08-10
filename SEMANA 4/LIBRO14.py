"""Diccionario en Python"""

"""
del: elmina un key y su valor del diccionario
"""

estudiante = {"nombre": "Matías", "edad": 26, "promedio":17}

estudiante["distrito"] = "Miraflores"

del estudiante["edad"]
del estudiante["promedio"]

print("Diccionario actualizado: {}".format(estudiante))

estudiante_alfa = {"nombre": "Matías", "edad": 26, "notas":[12, 16, 11, 18, 10], "padres": {"papa": "Luis", "mama": "Valeria"}}