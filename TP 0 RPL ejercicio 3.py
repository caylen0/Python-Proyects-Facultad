"""Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos.
Por ejemplo, si recibe los números 1,5,-2,-4, debe devolver 8, que es el producto mas grande
que se puede obtener entre ellos (-2 * -4 = 8)."""

def maximo_producto(num_1, num_2, num_3, num_4)-> int:
    maximo_num1 = maximo_2 (num_1, num_2, num_3, num_4)
    maximo_num2 = maximo_2(num_2, num_1, num_3, num_4)
    maximo_num3 = maximo_2(num_3, num_2, num_1, num_4)
    maximo_num4 = maximo_2(num_4, num_2, num_3, num_1)
    maximo_general: int = 0
    if maximo_num1 >= maximo_num2 and maximo_num1 >= maximo_num3 and maximo_num1 >= maximo_num4:
        maximo_general = maximo_num1
    if maximo_num2 >= maximo_num1 and maximo_num2 >= maximo_num3 and maximo_num2 >= maximo_num4:
        maximo_general = maximo_num2
    if maximo_num3 >= maximo_num2 and maximo_num3 >= maximo_num1 and maximo_num3 >= maximo_num4:
        maximo_general = maximo_num3
    if maximo_num4 >= maximo_num2 and maximo_num4 >= maximo_num3 and maximo_num4 >= maximo_num1:
        maximo_general = maximo_num4
    return maximo_general

def maximo_2 (num_1, num_2, num_3, num_4) -> int:
    resultado_1 = num_1 * num_2
    resultado_2 = num_1 * num_3
    resultado_3 = num_1 * num_4
    maximo: int = 0
    if resultado_1 > resultado_2 and resultado_1 > resultado_3:
        maximo = resultado_1
    elif resultado_2 > resultado_1 and resultado_2 > resultado_3:
        maximo = resultado_2
    else:
        maximo = resultado_3
    return maximo

def main() -> None:
    print("El maximo producto es: ")
    print(maximo_producto(1, 5, -2, -4))

main()