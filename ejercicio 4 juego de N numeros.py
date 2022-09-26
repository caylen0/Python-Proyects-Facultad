"""Ejercicio 4(Posiblemente de tarea):
Se pide hacer un programa que ingrese 8 juegos de 𝑛𝑛 valores positivos
cada uno. Considerar una condición de corte para el flujo de números.
Calculando el promedio de cada juego, el máximo de cada juego y el
mínimo de todos los juegos.
Donde en cada juego se deberá calcular:
• El máximo número ingresado.
• El mínimo número ingresado.
• El promedio de cada juego.
• El mínimo de todos los juegos."""

CERRAR_PROGRAMA: int = -1
CANTIDAD_DE_JUEGOS: int = 8
minimo_total: int = 0
cantidad_de_numeros: int = 0
suma_de_numeros: int = 0
juego : int

for juego in range(1,CANTIDAD_DE_JUEGOS, +1):
    numero: int = int(input("\n INGRESE UN NUMERO POSITIVO: \n"))
    cantidad_de_numeros = 0
    suma_de_numeros = 0
    while numero <= 0:
        numero: int = int(input("\n Numero invalido, INGRESE UN NUMERO POSITIVO: \n"))

    minimo: int = numero
    maximo: int = numero

    while numero > 0:
        cantidad_de_numeros = cantidad_de_numeros + 1
        suma_de_numeros = suma_de_numeros + numero
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
        numero = int(input('Ingrese un número positivo. Si el juego no tiene más números ingrese un número negativo o el 0 :'))
    if minimo < minimo_total:
        minimo_total = minimo

    print("\n En su juego, el maximo es: ", maximo, "y el minimo es: ", minimo)
    print("\n El promedio del juego es: ", suma_de_numeros / cantidad_de_numeros)

print("El minimo de todos los juegos es: ", minimo_total)