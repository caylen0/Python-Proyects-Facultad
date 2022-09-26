"""Se dice que dos números A y B se llaman números amigos si la suma de los divisores de A es igual B y
 la suma de los divisores de B es igual a A.
NOTA: No se debe tener en cuenta al número como su propio divisor."""

def calcular_suma_de_divisores(numero : int) -> int:
    suma_divisores: int = 0
    for posible_divisor in range(1, numero):
        if numero % posible_divisor == 0:
            suma_divisores = suma_divisores + posible_divisor
    return suma_divisores

def numeros_amigos(a: int, b: int) -> bool:
    suma_divisores_A: int = calcular_suma_de_divisores(a)
    suma_divisores_B: int = calcular_suma_de_divisores(b)

    return suma_divisores_A == b and suma_divisores_B == a

def main() -> None:
    print(numeros_amigos(220, 284)

main()
