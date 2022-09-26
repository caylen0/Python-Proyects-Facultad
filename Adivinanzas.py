"""Crear un programa que permita este funcionamiento de juego:
Un usuario1 va a ingresar una palabra y un usuario2 va a tener tres intentos para adivinar cuántas letras contiene esa palabra.
En caso de que el usuario2 adivine la cantidad; se printeará: "¡Muy bien!"
En caso de que el usuario2 adivine la cantidad DOS VECES; se printeará: "que genio :) "
En caso de que el usuario2 adivine la cantidad TRES VECES se printeara: "que level"
En caso de que el usuario2 no adivine la cantidad ninguna vez; se printeará: "Vuelva prontos; esta vez no se pudo"""

palabra = ""
cantidad_de_letras = 0

palabra = str(input("Ingrese la palabra que el usuario 2 debera adivinar la cantidad de letras que posee: "))

intento_1: int = int(input("Ingrese la cantidad de letras que piensa que el Usuario 1, puso como palabra. (Vas a tener 3 chances) "))
intento_2: int = int(input("Segunda chance: "))
intento_3: int = int(input("Ultima chance: "))

cantidad_de_letras = len(palabra)

if(intento_1 == intento_2 == intento_3 == cantidad_de_letras):
    print("que level")
elif((intento_1 == cantidad_de_letras and intento_2 == cantidad_de_letras) or (intento_1 == cantidad_de_letras and intento_3 == cantidad_de_letras) or
     (intento_2 == cantidad_de_letras and intento_3 == cantidad_de_letras)):
     print("Que genioo :) ")
elif (intento_1 == cantidad_de_letras or intento_2 == cantidad_de_letras or intento_3 == cantidad_de_letras):
    print("¡Muy bien!")
else:
    print("vuelva prontos")