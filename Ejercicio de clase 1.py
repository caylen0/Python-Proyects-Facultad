import random

"""Escribir un programa en Pyhton que solicite 5 numeros enteros al usuario. 
el mismo debe indicar si entre ellos hay numeros duplicadoso no, imprimiento 
en pantalla "HAY DUPLICADOS" o "SON TODOS DISTINTOS"""

numero_1: int = random.randint(0, 20)
numero_2: int = random.randint(0, 20)
numero_3: int = random.randint(0, 20)
numero_4: int = random.randint(0, 20)
numero_5: int = random.randint(0, 20)

son_distintos: bool = True     #Asumo que todos los numeros van a ser iguales

if ((numero_1 == numero_2) or (numero_1 == numero_3) or (numero_1 == numero_4) or (numero_1 == numero_5)):
    son_distintos = False

elif ((numero_2 == numero_3) or (numero_2 == numero_4) or (numero_2 == numero_5)):
    son_distintos = False

elif ((numero_3 == numero_4) or (numero_3 == numero_5)):
    son_distintos = False

elif ((numero_4 == numero_5)):
    son_distintos = False

mensaje: str = "SON TODOS DISTINTOS" if (son_distintos) else "HAY DUPLICADOS"

print(mensaje)

print("Numero 1: ", numero_1)
print("Numero 2: ", numero_2)
print("Numero 3: ", numero_3)
print("Numero 4: ", numero_4)
print("Numero 5: ", numero_5)

