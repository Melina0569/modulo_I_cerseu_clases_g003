"""Uso de la condicional 'if'"""
"""if ternarios"""

"""
Requisitos:
- Ingresar por teclado el sueldo de un empleado
- Si el sueldo es mayor a 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo iene bonificación este año y será de:
sueldo_final", sueldo_final = sueldo + 20% sueldo

1/2 pto sobre su 2da práctica
"""

sueldo = float(input("Ingresar sueldo del empleado: "))

sueldo_final = sueldo + sueldo * 0.20

mensaje = ("Su sueldo no tiene bonificación" if sueldo > 4000 else "Su sueldo tiene una bonificación este año y será de: {}".format(sueldo_final))

print(mensaje)


