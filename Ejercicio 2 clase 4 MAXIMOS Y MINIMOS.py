"""Escribe un prorgrama en Python que solicite al usuario 5 números enteros.
Luego imprimir el máximo y el mínimo de los valores ingresados.
El programa deberá permitir el ingreso de valores iguales."""


numero_1: int = int(input("Ingrese el primer numero: "))
numero_2: int = int(input("Ingrese el segundo numero: "))
numero_3: int = int(input("Ingrese el tercer numero: "))
numero_4: int = int(input("Ingrese el cuarto numero: "))
numero_5: int = int(input("Ingrese el quinto numero: "))

if ((numero_1 >= numero_2) and (numero_1 >= numero_3) and (numero_1 >= numero_4) and (numero_1 >= numero_5)):
      print("EL PRIMER NUMERO ES MAXIMO")

if ((numero_2 >= numero_1) and (numero_2 >= numero_3) and (numero_2 >= numero_4) and (numero_2 >= numero_5)):
      print("EL SEGUNDO NUMERO ES MAXIMO")

if ((numero_3 >= numero_1) and (numero_3 >= numero_2) and (numero_3 >= numero_4) and (numero_3 >= numero_5)):
      print("EL TERCER NUMERO ES MAXIMO")

if ((numero_4 >= numero_1) and (numero_4 >= numero_2) and (numero_4 >= numero_3) and (numero_4 >= numero_5)):
      print("EL CUARTO NUMERO ES MAXIMO")

if ((numero_5 >= numero_1) and (numero_5 >= numero_2) and (numero_5 >= numero_3) and (numero_5 >= numero_4)):
      print("EL QUINTO NUMERO ES MAXIMO")

# AHORA LO HAGO CON LOS MINIMOS

if ((numero_1 <= numero_2) and (numero_1 <= numero_3) and (numero_1 <= numero_4) and (numero_1 <= numero_5)):
      print("EL PRIMER NUMERO ES MINIMO")

if ((numero_2 <= numero_1) and (numero_2 <= numero_3) and (numero_2 <= numero_4) and (numero_2 <= numero_5)):
      print("EL SEGUNDO NUMERO ES MINIMO")

if ((numero_3 <= numero_1) and (numero_3 <= numero_2) and (numero_3 <= numero_4) and (numero_3 <= numero_5)):
      print("EL TERCER NUMERO ES MINIMO")

if ((numero_4 <= numero_1) and (numero_4 <= numero_2) and (numero_4 <= numero_3) and (numero_4 <= numero_5)):
      print("EL CUARTO NUMERO ES MINIMO")

if ((numero_5 <= numero_1) and (numero_5 <= numero_2) and (numero_5 <= numero_3) and (numero_5 <= numero_4)):
      print("EL QUINTO NUMERO ES MINIMO")
