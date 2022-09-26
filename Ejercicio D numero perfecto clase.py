""" Extra: Tomar uno de los incisos anteriores y verificar la condición
pedida para todos los números en un intervalo (1, 𝑛𝑛] donde 𝑛𝑛 es un
número ingresado por el usuario."""

numero_ingresado: int = int(input("Ingrese un numero: \n"))

suma: int = 0



for numero_evaluado in range(1, numero_ingresado + 1):
    suma = 0
    for divisor in range(1, numero_evaluado): #Se puede inicializar range con el numero que deseo, poniendolo (numero que quiero, variable)
        if numero_evaluado % divisor == 0:
            suma = suma + divisor

    if numero_evaluado == suma:
        print("\n El numero", numero_evaluado, "es Perfecto") # perfecto es igual a la suma de sus divisores
    else:
        print("\n El numero", numero_evaluado, "NO es perfecto ")
