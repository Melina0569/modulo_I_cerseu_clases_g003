"""Programación funcional"""

"""
Requisitos:
- Crear una función que multiplcará 4 valores (int y floats)
- La función tendrá un parámetro o que contendrá un valor
- Mostrar 2 casos donde ese ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando

correo: docente.cerseu.unmsm@gmail.com
asunto: partipación para práctica 02
tiempo máximo de entrega: media noche
"""

# Función que multiplica 4 valores
def multiplicar_cuatro(a, b, c, d, parametro):
    resultado = a * b * c * d
    print("Multiplicación: {}".format(resultado))

    # Intentamos modificar el parámetro
    if isinstance(parametro, list):  # si es lista (mutable)
        parametro.append(resultado)
    else:  # si es int o float (inmutable)
        parametro += resultado

    print("Parámetro dentro de la función: {}".format(parametro))


# Caso 1: El parámetro NO se ve afectado (int → inmutable)
valor_int = 10
multiplicar_cuatro(2, 3, 1.5, 4, valor_int)
print("Parámetro fuera de la función (int): {}".format(valor_int))
print("-" * 50)

# Caso 2: El parámetro SÍ se ve afectado (lista → mutable)
valor_lista = [10]
multiplicar_cuatro(2, 3, 1.5, 4, valor_lista)
print("Parámetro fuera de la función (lista): {}".format(valor_lista))