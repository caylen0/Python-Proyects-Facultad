"""Pedirle al usuario que ingrese 10 numeros y retornar la suma de los mismos"""

suma : int = 0

for i in range(10):
    numero : int = int(input("Ingrese un numero: "))
    resultado = suma + numero

print("El resultado de la suma es: ", resultado)

