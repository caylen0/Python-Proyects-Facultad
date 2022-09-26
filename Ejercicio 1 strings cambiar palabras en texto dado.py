#EJERCICIO 1
"""Escribir un programa que permita cambiar todas las palabras que indique el usuario en un texto dado."""


palabra_a_buscar: str = ""
palabra_a_reemplazar: str = ""
texto: str = "este es un texto de ejemplo para el ejercicio 1 "
cerrar_programa: bool = False

print ("\n Este es el texto asignado: ",texto)
respuesta_usuario: str = input("\n Desea modificar el texto? SI/NO: ").upper()

if respuesta_usuario == "NO":
    cerrar_programa = True

while cerrar_programa == False:
    palabra_a_buscar = input("\n Que palabra quiere buscar?: ").lower()
    if texto.find(palabra_a_buscar) == -1:
        print("\n No se encontro la palabra a buscar")
    else:
        palabra_a_reemplazar = input("\n Por que palabra quiere reemplazar: ").lower()
        texto = texto.replace(palabra_a_buscar , palabra_a_reemplazar)
        print("\n El texto modificado es: ", texto)
    respuesta_usuario: str = input("\n Desea modificar el texto? SI/NO: ").upper()
    if respuesta_usuario == "NO":
        cerrar_programa = True
