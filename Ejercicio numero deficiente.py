""" Crear un programa que permita al usuario ingresar un número e
indicar si es un número deficiente. Un número es deficiente cuando
es MAYOR a la suma de todos sus divisores propios (exceptuándose
así mismo).
Por ejemplo:
 14 es un número deficiente porque sus divisores
 son: 1,2,7 → 10 < 14."""

numero_ingresado: int = int(input("Ingrese un numero: \n"))

suma: int = 0

i: int = 1

for i in range(1, numero_ingresado): #Se puede inicializar range con el numero que deseo, poniendolo (numero que quiero, variable)
    if numero_ingresado % i == 0:
        suma = suma + i

if numero_ingresado > suma:
    print("\n El numero ingresado es Deficiente")
elif numero_ingresado == suma:
    print("\n El numero ingresado es Perfecto") # perfecto es igual a la suma de sus divisores
else:
    print("\n El numero ingresado NO es Deficiente porque: ", suma, "es mayor a: ", numero_ingresado)
    print("\n El numero es Abundante") #abundante es menor a la suma de sus divisores