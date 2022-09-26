"""Crear una calculadora de 4 funcionalidades (+, −, /,∗). Donde se le
pregunte al usuario que operación desea realizar y luego preguntarle por
dos números para realizar dicha operación. También debe de haber una
opción para cerrar el programa."""

cerrar_programa: str = "5"

print("\n CALCULADORA")
respuesta_usuario: str = input("\n QUE OPERACION DESEA REALIZAR?:"
      "\n 1. SUMA"
      "\n 2. RESTA"
      "\n 3. MULTIPLICACION"
      "\n 4. DIVISION"
      "\n 5. CERRAR EL PROGRAMA\n"
                               "\n")

while respuesta_usuario != cerrar_programa:
      if respuesta_usuario == "1":
            numero1: int = int(input("\n INGRESE EL PRIMER NUMERO: "))
            numero2: int = int(input("\n INGRESE EL SEGUNDO NUMERO: "))
            print("\n EL RESULTADO DE LA SUMA ES: ", numero1 + numero2)
      elif respuesta_usuario == "2":
            numero1: int = int(input("\n INGRESE EL PRIMER NUMERO: "))
            numero2: int = int(input("\n INGRESE EL SEGUNDO NUMERO: "))
            print("\n EL RESULTADO DE LA RESTA ES: ", numero1 - numero2)
      elif respuesta_usuario == "3":
            numero1: int = int(input("\n INGRESE EL PRIMER NUMERO: "))
            numero2: int = int(input("\n INGRESE EL SEGUNDO NUMERO: "))
            print("\n EL RESULTADO DE LA MULTIPLICACION ES: ", numero1 * numero2)
      elif respuesta_usuario == "4":
            numero1: int = int(input("\n INGRESE EL PRIMER NUMERO: "))
            numero2: int = int(input("\n INGRESE EL SEGUNDO NUMERO: "))
            print("\n EL RESULTADO DE LA DIVISION ES: ", numero1 / numero2)
      else: print("INGRESE UNA OPCION CORRECTA")
      respuesta_usuario: str = input("\n QUE OPERACION DESEA REALIZAR?:"
                                     "\n 1. SUMA"
                                     "\n 2. RESTA"
                                     "\n 3. MULTIPLICACION"
                                     "\n 4. DIVISION"
                                     "\n 5. CERRAR EL PROGRAMA\n "
                                     "\n")

if respuesta_usuario == cerrar_programa:
      print("\n EL PROGRAMA SE CERRARA.")