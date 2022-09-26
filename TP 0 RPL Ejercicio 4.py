"""Se pide crear un programa donde el usuario ingrese el día y mes de su cumpleaños y el programa le imprimir por pantalla a qué signo del zodíaco corresponde.

Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo.
Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero."""

def signo_zodiaco(dia: int, mes: int) ->str:
    signo: str
    if ((mes == 1) and dia >= 21) or ((mes == 2) and dia <= 19):
        signo = "Acuario"
    elif ((mes == 2) and dia >= 20) or ((mes == 3) and dia <= 20):
        signo = "Piscis"
    elif ((mes == 3) and dia >= 21) or ((mes == 4) and dia <= 20):
        signo = "Aries"
    elif ((mes == 4) and dia >= 21) or ((mes == 5) and dia <= 20):
        signo = "Tauro"
    elif ((mes == 5) and dia >= 20) or ((mes == 6) and dia <= 21):
        signo = "Geminis"
    elif ((mes == 6) and dia >= 22) or ((mes == 7) and dia <= 23):
        signo = "Cancer"
    elif ((mes == 7) and dia >= 24) or ((mes == 8) and dia <= 23):
        signo = "Leo"
    elif ((mes == 8) and dia >= 24) or ((mes == 9) and dia <= 23):
        signo = "Virgo"
    elif ((mes == 9) and dia >= 24) or ((mes == 10) and dia <= 22):
        signo = "Libra"
    elif ((mes == 10) and dia >= 23) or ((mes == 11) and dia <= 22):
        signo = "Escorpio"
    elif ((mes == 11) and dia >= 22) or ((mes == 12) and dia <= 21):
        signo = "Sagitario"
    else:
        signo = "Capricornio"

    return signo
def main() -> None:
    dia: int = int(input("Ingrese el dia: "))
    while ((dia>32) or (dia<=0)):
        dia: int = int(input("Ingrese el dia: "))
    mes: int = int(input("Ingrese el mes: "))
    while ((mes>12) or (mes<=0)):
        mes: int = int(input("Ingrese el mes: "))

    print(signo_zodiaco(dia, mes))

main()

















