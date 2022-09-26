

def pasaje_a_segundos (horas: int, minutos: int, segundos: int) -> int:
    pasaje = (horas * 3600) + (minutos * 60) + segundos
    return pasaje

def suma_intervalos (intervalo1: int , intervalo2: int ) -> int:
    suma: int = intervalo1 + intervalo2
    return suma

def main() -> None:
    print("PRIMER INTERVALO")
    horas: int = int(input("\n INGRESE LA HORA: \n"))
    minutos: int = int(input("\n INGRESE LOS MINUTOS: \n"))
    segundos: int = int(input("\n INGRESE LOS SEGUNDOS: \n"))
    print("SEGUNDO INTERVALO")
    horas2: int = int(input(" \n INGRESE LA HORA: \n"))
    minutos2: int = int(input("\n INGRESE LOS MINUTOS: \n"))
    segundos2: int = int(input("\n INGRESE LOS SEGUNDOS: \n"))

    resultado: int = pasaje_a_segundos(horas, minutos, segundos)
    resultado_2: int = pasaje_a_segundos(horas2, minutos2, segundos2)

    total_suma: int = suma_intervalos(resultado , resultado_2)
    horas_resultado: int = int(total_suma / 3600)
    minutos_resultado: int = int((total_suma % 3600) / 60)
    segundos_resultado: int = total_suma % 3600 % 60

    print(f"{horas}hs {minutos}min {segundos}seg = {resultado}seg")
    print(f"{horas2}hs {minutos2}min {segundos2}seg = {resultado_2}seg")
    print(f"{horas}hs {minutos}min {segundos}seg + {horas2}hs {minutos2}min {segundos2}seg = {horas_resultado}hs {minutos_resultado}min {segundos_resultado}seg")

main()