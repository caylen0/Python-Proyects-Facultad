#EJERCICIO 2

"""Escribir un programa que permita desencriptar un texto dado.
El encriptado del código es el siguiente
El mensaje está escrito cada 3 caracteres comenzando por el tercero.
Cada número corresponde a una vocal (1=a,2=e,3=i,4=o,5=u)
Los espacios se representan con “&”
Texto="avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"
"""

texto: str = "avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"
texto = texto.replace("1", "a")
texto = texto.replace("2", "e")
texto = texto.replace("3", "i")
texto = texto.replace("4", "o")
texto = texto.replace("5", "u")
texto = texto.replace("&", " ")

print(texto[2::3])