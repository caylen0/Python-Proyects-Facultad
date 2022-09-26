"""Se debe pedir al usuario (Vicky) si quiere agregar un gato más al ataque contra Timmy,
cuando ya esté satisfecha se deberá mostrar la cantidad de gatos que atacaron a Timmy."""

respuesta: str = input("DESEA AGREGAR MAS GATOS? SI/NO: ")

gatos: int = 0

while (respuesta == "SI"):
    gatos = gatos + 1
    respuesta = input("DESEA AGREGAR MAS GATOS? SI/NO: ")

if (respuesta == "NO"):
    print("La cantidad de gatos que atacaron a timmy son: ", gatos)