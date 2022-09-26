"""Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos de b.
El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso de que no lo sea,
solicitarlo nuevamente (hasta que se ingrese algo correcto)."""

def main() -> None:
    input_numero_A: str = input("Ingrese el número 'a': ") #cantidad de veces que muestra el multiplo
    while not(input_numero_A.isnumeric()) or input_numero_A == '0': #pido que si no es numerico, lo vuelva a pedir
        input_numero_A: str = input("Ingrese el número 'a': ")
    input_numero_B: str = input("Ingrese el número 'b': ") #numero a averigar sus multiplos
    while not(input_numero_B.isnumeric()) or input_numero_B == '0':
        input_numero_B: str = input("Ingrese el número 'b': ")

    numero_A: int = int(input_numero_A) #paso la variable input_numero_A de str a un int
    numero_B: int = int(input_numero_B)
    multiplo : int = 0

    for numero in range(1, numero_A + 1):
        multiplo = multiplo + numero_B
        print(multiplo)

main()