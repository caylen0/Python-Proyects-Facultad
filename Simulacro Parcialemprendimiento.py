""" es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además
de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad
general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500

El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de
un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- Crear un menú que permita el acceso a los siguientes puntos.
b- Modificación de cursos. Se podrá modificar la siguiente infomación de los cursos. Nombre, cantidad de días,
costo.
c- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
d- Cargado de asistentes a los cursos definidos.
e- Mostrar el listado de todos los cursos y sus respectivos asistentes. Ordenados por nombre de curso en forma
ascendente."""


def modificar_cursos(cursos: list) -> list:
	respuesta_curso_a_modificar: int = int(input(("\n QUE CURSO DESEA MODIFICAR?:"
	                                              "\n 0. Compost"
	                                              "\n 1. Niños y el medioambiente"
	                                              "\n 2. Tu huerta organica \n")))
	respuesta_campo_a_modificar: int = int(input("\n QUE CAMPO DESEA MODIFICAR?: "
	                                             "\n 0. Nombre"
	                                             "\n 1. Dias"
	                                             "\n 2. Costo \n"))

	if respuesta_campo_a_modificar == 0:
		nombre: str = input(f"Ingrese el nuevo nombre para el curso: ")
		cursos[respuesta_curso_a_modificar][0] = nombre
		print(f"El nombre del curso actualizado es:: {cursos[respuesta_campo_a_modificar][0]}")
	if respuesta_campo_a_modificar == 1:
		dias: int = int(input(f"Actualice la cantidad de dias del curso: "))
		cursos[respuesta_curso_a_modificar][1] = dias
		print(f"La duracion en dias es: {cursos[respuesta_campo_a_modificar][1]}")
	if respuesta_campo_a_modificar == 2:
		costo: int = int(input(f"Actualice el precio del curso: "))
		cursos[respuesta_curso_a_modificar][2] = costo
		print(f"El costo actualizado es: {cursos[respuesta_campo_a_modificar][2]}")

	return cursos

def mostrar_cursos_caros(cursos: list)-> None:
	precio: int = 1150
	for curso in cursos:
		if curso[2] > precio:
			print(f"El curso {curso[0]} tiene un costo mayor a $1150")


def cargar_asistentes(cursos: list) -> list:
	respuesta_carga_usuarios: int = int(input(("\n A QUE CURSO DESEA CARGARLE ASISTENTES?:"
	                                           "\n 0. Aprende a hacer tu propio compost"
	                                           "\n 1. Niños y el medioambiente"
	                                           "\n 2. Tu huerta organica \n")))

	nombre_asistente: str = input(f"Cargue el nombre del asistente: ")
	cursos[respuesta_carga_usuarios][3].append(nombre_asistente)
	carga_de_asistentes: str = input(f"Desea agregar otro asistente? SI/NO: ").upper()
	while carga_de_asistentes == 'SI':
		carga_asistente: str = input(f"Cargue el nombre de otro asistente: ")
		cursos[respuesta_carga_usuarios][3].append(carga_asistente)
		carga_de_asistentes: str = input(f"Desea agregar otro asistente? SI/NO: ").upper()

	return cursos

def mostrar_cursos_con_asistentes(cursos: list) -> None:
	for curso in cursos:
		print(f"El nombre del curso es: {curso[0]}")
		print(f"La duracion del curso es: {curso[1]}")
		print(f"El costo del curso es: {curso[2]}")
		for asistente in curso[3]:
			print(f"El nombre del asistente es: {asistente}")

def main() -> None:
	cursos: list(list) = [[' Aprende a hacer tu propio compost', 1, 950, []],
	                      ['Los niños y el medioambiente(para padres e hijes)', 2, 990, []],
	                      ['Tu huerta organica', 4, 2500, []]]
	salir: str = '5'
	respuesta_usuario: str = input("\n QUE OPCION DESEA REALIZAR?:"
	                               "\n 1. MODIFICAR CURSOS"
	                               "\n 2. LISTAR CURSOS CUYO COSTO ES MAYOR A $1150"
	                               "\n 3. CARGAR ASISTENTES A LOS CURSOS DEFINIDOS"
	                               "\n 4. MOSTAR LISTADO DE TODOS LOS CURSOS CON SUS RESPECTIVOS ASISTENTES"
	                               "\n 5. SALIR \n")

	while respuesta_usuario != salir:
		if respuesta_usuario == '1':
			cursos = modificar_cursos(cursos)
		if respuesta_usuario == '2':
			mostrar_cursos_caros(cursos)
		if respuesta_usuario == '3':
			cursos = cargar_asistentes(cursos)
		if respuesta_usuario == '4':
			mostrar_cursos_con_asistentes(cursos)

		respuesta_usuario: str = input("\n QUE OPCION DESEA REALIZAR?:"
		                               "\n 1. MODIFICAR CURSOS"
		                               "\n 2. LISTAR CURSOS CUYO COSTO ES MAYOR A $1150"
		                               "\n 3. CARGAR ASISTENTES A LOS CURSOS DEFINIDOS"
		                               "\n 4. MOSTAR LISTADO DE TODOS LOS CURSOS CON SUS RESPECTIVOS ASISTENTES"
		                               "\n 5. SALIR \n")

	if respuesta_usuario == '5':
		print(f"Se va a cerrar el programa")

main()
