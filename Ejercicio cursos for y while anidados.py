"""Ejercicio ciclos anidados.
Se tienen 10 cursos de 30 alumnos de los cuales se quiere saber lo siguiente:
1. El promedio de cada curso
2. El curso que mayor promedio tiene
3. El nombre del alumno que mayor nota obtuvo (se supone único) y a que curso pertenece"""

#para punto 1:
cantidad_de_cursos: int = 2
cantidad_de_alumnos: int = 2
suma_notas: int = 0
promedio_del_curso: int = 0

# para punto 2:
promedio_maximo: int = 0
nombre_del_curso_prom_max: int = 0

#para punto 3:
nombre_del_alumno_prom_max: str = ""
nombre_del_curso_con_alumno_con_max_nota: int = 0
nota_maxima: int = 0

for curso in range(cantidad_de_cursos):
    suma_notas = 0

    for alumno in range(cantidad_de_alumnos):
        nombre_alumno = input("Ingrese el nombre del alumno: \n")
        nota = int(input("Ingrese la nota del alumno: \n"))
        suma_notas = suma_notas + nota

        if (nota > nota_maxima):
            nota_maxima = nota
            nombre_del_alumno_prom_max = nombre_alumno
            nombre_del_curso_con_alumno_con_max_nota = curso


    promedio_del_curso = suma_notas / cantidad_de_alumnos
    print("el promedio del curso numero ",curso + 1," es:", promedio_del_curso,"\n")

    if(promedio_del_curso > promedio_maximo):
        promedio_maximo = promedio_del_curso
        nombre_del_curso_prom_max = curso


print("El curso ",nombre_del_curso_prom_max," es el de mayor promedio con nota: ", promedio_maximo,"\n")

print("El alumno que mayor nota obtuvo: ", nombre_del_alumno_prom_max, "perteneciente al curso: ",
      nombre_del_curso_con_alumno_con_max_nota, " con nota: ",nota_maxima,"\n")