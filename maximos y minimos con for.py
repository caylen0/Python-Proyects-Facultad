"""Escribe un prorgrama en Python que solicite al usuario 5 números enteros.
Luego imprimir el máximo y el mínimo de los valores ingresados.
El programa deberá permitir el ingreso de valores iguales."""


numero_1: int = int(input("Ingrese el primer numero: "))
numero_2: int = int(input("Ingrese el segundo numero: "))
numero_3: int = int(input("Ingrese el tercer numero: "))
numero_4: int = int(input("Ingrese el cuarto numero: "))
numero_5: int = int(input("Ingrese el quinto numero: "))

lista_numeros = [numero_1,numero_2,numero_3,numero_4,numero_5]

maximo = 0
minimo = 0

for numero in lista_numeros:
      if ((numero >= numero_1) and (numero >= numero_2) and (numero >= numero_3) and (numero >= numero_4) and (numero >= numero_5)):
            maximo = numero

for numero in lista_numeros:
      if ((numero <= numero_1) and (numero <= numero_2) and (numero <= numero_3) and (numero <= numero_4) and (numero <= numero_5)):
            minimo = numero

print("el numero maximo es ",maximo,"; y el minimo es: ",minimo)