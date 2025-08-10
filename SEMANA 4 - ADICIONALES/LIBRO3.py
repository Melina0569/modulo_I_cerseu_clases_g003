"""Uso de 'for' """
ingenierias = ["Software", "Sistemas", "Química", "Mecánica", "Mecatrónica", "Industrial"]
print("Tamaño de mi lista: {}".format(len(ingenierias)))

i = 0

for ingenieria in ingenierias:
    print("Ing. ", ingenieria)
    print("Valor de i: ", i)
    i = i + 1 #Aumento del número inicia de i en 1
    print("Número de iteración: ", i)