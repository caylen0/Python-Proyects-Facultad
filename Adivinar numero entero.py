"""Realizar un programa que permita jugar a adivinar un número entero.
El participante A elige el número a adivinar, y luego hace jugar al
participante B, el cual deberá intentar adivinarlo arriesgando números.
El programa debe guiar al participante B indicándole, en cada intento, si el
número arriesgado es mayor o menor al definido por el participante A.
El juego debe concluir al acertar el número o superar los 20 intentos.
Al acertar el número debe indicar la cantidad de intentos que fueron
utilizados para lograrlo.
En caso de no haber conseguido el objetivo, debe indicarle que ha superado
los 20 intentos. """

INTENTOS: int = 20
numero_para_adivinar: int = int(input("Ingrese un numero para comenzar: "))
numero_de_intentos: int = 0
numero_arriesgado: int = int(input("\n Ingrese un numero: "))

while (numero_arriesgado != numero_para_adivinar) and (numero_de_intentos < INTENTOS):
    numero_de_intentos = numero_de_intentos + 1
    if numero_arriesgado > numero_para_adivinar:
        print("El numero arriesgado", numero_arriesgado, "es mayor al numero definido por el participante A")
    elif numero_arriesgado < numero_para_adivinar:
        print("El numero arriesgado", numero_arriesgado, "es menor al numero definido por el participante A")
    numero_arriesgado = int(input("\n Ingrese un numero: "))

if numero_arriesgado == numero_para_adivinar:
    print("\n Acertaste el numero con esta cantidad de intentos: ", numero_de_intentos + 1)
else: print("Se terminaron los intentos")

