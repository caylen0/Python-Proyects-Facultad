"""Búsqueda de extremos:
Solicitar el ingreso de n números y hallar el máximo.
Solicitar el ingreso de n números y hallar el mínimo."""

numero: int = 0
maximo: int = 0
minimo: int = 9999999999
respuesta: str = "SI"

while (respuesta == "SI"):
    numero = int(input("Ingrese un numero: "))
    if (numero > maximo):
        maximo = numero
    if (numero < minimo):
        minimo = numero
    respuesta = input("QUIERE INGRESAR OTRO NUMERO? SI/NO: ")


print("El numero maximo es: ", maximo)
print("El numero minimo es: ", minimo)









