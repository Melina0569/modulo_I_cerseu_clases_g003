"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de enero y febrero (más de 1500)
3. Crear una variable donde se sumará el ingreso de los dos meses de enero y febrero
4. Mostrar en pantalla el mensaje de:

"Hola soy 'nombre' mi profesion es 'profesion' y mi remuneración acumulada es de 'remuneración:total''"
"""

nombre = "Melina"
profesion = "Investigación Operativa"
ciudad = "Lima"
rem1 = 2500
rem2 = 2700
rem_total = rem1 + rem2
print("Hola, mi nombre es {}, mi profesion es {} y soy de la ciudad de {}. Mi remuneración total es {}".format(nombre,profesion,ciudad,rem_total))