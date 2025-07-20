"""

Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string con contenido netamente numérico
   y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica (conversiones, realizarla si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la
   variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
6. Obtener una potencia usando una de las variables flotantes como base y la variable entera como potencia

Nota:
Las variables string pueden ser tu nombre y apellido

Hora de entrega máxima : 7 pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Ejercicio Participación - Semana 02
Adjuntar: archivo.py
En la parte superior dejar su nombre y apellido: como comentario


"""

int_1 = 15
int_2 = 10

float_1 = 5.5
float_2 = 12.5

str_1 = "Buen día"
str_2 = "50609"

bool_1 = True

suma1 = int_1 + int(str_2)
print("La suma de {} y  {} es: {}".format(int_1, str_2,suma1))

suma2 = int_1 + int_2 + int(str_2) + float_1
print("Suma total: {}".format(suma2))

modulo = int_1 % int_2
print("Módulo: {}".format(modulo))

division = int_1 // int_2
print("Division entera: {}".format(division))

potencia = float_2 ** int_2
print("Potencia: {}".format(potencia))



