"""Diccionarios en Python"""

"""
values: obtener los valores de los keys de un diccionario
"""
base_datos = {"nombre": "Mysql", "tipo": "BD Relacional"}

"""Conversión de diccionarios a listas"""
base_datos_list = list(base_datos)
print("Diccionario convertido en lista: {}".format(base_datos_list))

base_datos_values = list(base_datos.values())
print(base_datos_values)

base_datos_keys = list(base_datos.keys())
print(base_datos_keys)

base_datos_items = list(base_datos.items())
print(base_datos_items)