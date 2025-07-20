"""
-Caso: Calculadora de propinas
 Crea un programa que permita ingresar el total de una cuenta en un restaurante,
 el porcentaje de propina que desea dejar el cliente y el número de personas que
 dividirán la cuenta. El programa debe mostrar:
 El monto total con propina.
 El monto que debe pagar cada persona (con 2 decimales).
 Un mensaje será personalizado, indicará si el monto individual supera los 100
 soles, mostrando un mensaje de advertencia si es el caso.
 Entrada esperada (por input):
 Total de la cuenta: float
 Porcentaje de propina: float
 Número de personas: int
 Salida ejemplo (output):
 Monto total con propina: S/. 230.00
 Cada persona debe pagar: S/. 115.00
 ¡Advertencia! El monto por persona supera los S/. 100

"""

totalcuenta = float(input("Total de la cuenta S/: "))
porcentajepropina = float(input("Porcentaje de propina (%): "))
numeropersonas = int(input("Número de personas: "))

propina = totalcuenta * (porcentajepropina / 100)
totalpropina = totalcuenta + propina
montopersona = totalpropina / numeropersonas

print("Monto total con propina: S/. {}".format(totalpropina))
print("Cada persona debe realizarl el pago de S/. {}".format(montopersona))

if montopersona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")