"""
Intervención:
Requisitos:
- Dentro de una empresa se vaa solicitar pedir el nombre y apelldio del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y calculo del bono final de año, que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido', recibirá 'bono' soles de fin de año"

OJO:
* Hora máxima de entrega 7 pm
* Correo a enviar: docente.cerseu.unmsm@gmail.com
* Asunto: Intervención para práctica 02
* Adjuntar archivo .py y screemshot de resultados
"""

nombre = input('Ingrese el nombre del empleado: ')
apellido = input('Ingrese el apellido del empleado: ')
distrito = input('Ingrese el distrito donde reside el empleado: ')
sueldo = float(input('Ingrese el sueldo del empleado: '))

bono_final = (sueldo * 3) - (sueldo * 0.10)

empleado = {'Nombre': nombre, 'Apellido': apellido, 'Distrito': distrito, 'Bono final': bono_final}

nombre_empleado = empleado['Nombre']
apellido_empleado = empleado['Apellido']
BF_empleado = empleado['Bono final']

print("{} {}, recibirá {} soles de fin de año".format(nombre_empleado, apellido_empleado, BF_empleado))


