"""Yamila, la cosmetóloga furor en redes, tiene un consultorio donde realiza limpiezas y tratamientos para el cuidado
de la piel.
Debido a la alta demanda de sus pacientes y futuros pacientes, nos pidió que realicemos un programa que la ayude
con la planificación de su negocio. La información del paciente que Yami necesita analizar es la cantidad de consultas
asistidas y que tratamientos fueron realizados.
Asimismo, el catálogo de tratamientos que comercializa es el siguiente:
 - Higiene profunda $1500
 - Tratamiento Acné $1500
 - Tratamiento tensor con aparatología $1800
 - Tratamiento revitalizante $3000
Hacer un programa que:
 a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:
 - DNI
 - Nombre y Apellido
 - Cantidad de consultas asistidas
 - Tratamientos realizados (Tipo y cantidad. Puede ser ninguno)
 b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.
 c) Emita un reporte que informe el monto total de tratamientos vendidos.
 d) Emita un reporte que informe el total de pacientes nuevos y viejos.
 e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.
A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido únicamente a 1
consulta con el profesional. """

def ingresar_paciente(pacientes: list(list))-> list(list):
	respuesta: str = 'SI'
	contador_pacientes: int = 0
	while respuesta == 'SI':
		pacientes.append([])
		nombre: str = input(f"\n Ingrese el nombre del paciente: ")
		dni: int = int(input(f"\n Ingrese el dni del paciente: "))
		cantidad_de_consultas: int = int(input(f"\n Ingrese las consultas del paciente: "))
		tratamientos_realizados: list(tuple) = []
		respuesta_tratamientos: str = input(f"\n Desea agregar un tratamiento? SI/NO: ").upper()
		while respuesta_tratamientos == 'SI':
			tipo_tratamiento: str = input(f"\n Que tipo de tratamiento se realizo?: ").upper()
			cantidad_tratamiento: int = int(input(f"\n Cuantos tratamientos se relaizo el paciente?: ")).upper()
			tratamientos_realizados.append((tipo_tratamiento, cantidad_tratamiento))
			respuesta_tratamientos: str = input(f"\n Desea agregar un tratamiento? SI/NO: ").upper()
		pacientes[contador_pacientes].append(nombre)
		pacientes[contador_pacientes].append(dni)
		pacientes[contador_pacientes].append(cantidad_de_consultas)
		pacientes[contador_pacientes].append(tratamientos_realizados)
		contador_pacientes += 1
		respuesta: str = input(f"\n Desea agregar un paciente? SI/NO: ").upper()
	return pacientes

def mostrar_tratamiento_mas_solicitado(pacientes: list(list)) -> None:
	acumulador_higiene_profunda: int = 0
	acumulador_acne: int = 0
	acumulador_tensor: int = 0
	acumulador_revitalizante: int = 0
	for paciente in pacientes:
		for tratamiento_realizado in paciente[3]: #tupla de tipo y cantidad de tratamiento
			if tratamiento_realizado [0] == 'HIGIENE PROFUNDA':
				acumulador_higiene_profunda += tratamiento_realizado[1]
			if tratamiento_realizado[0] == 'TRATAMIENTO ACNE':
				acumulador_acne += tratamiento_realizado[1]
			if tratamiento_realizado[0] == 'TRATAMIENTO TENSOR CON APARATLOGIA':
				acumulador_tensor += tratamiento_realizado[1]
			if tratamiento_realizado[0] == 'TRATAMIENTO REVITALIZANTE':
				acumulador_revitalizante += tratamiento_realizado[1]
				#hastca aca queda funcion acumulador, despues la llamo para crear las otras funciones
	if acumulador_higiene_profunda >= acumulador_acne and acumulador_higiene_profunda >= acumulador_tensor and acumulador_higiene_profunda >= acumulador_revitalizante:
		print(f"El tratamiento con mayor realizacion es HIGIENE PROFUNDA")
	if acumulador_acne >= acumulador_higiene_profunda and acumulador_acne >= acumulador_tensor and acumulador_acne >= acumulador_revitalizante:
		print(f"El tratamiento con mayor realizacion es TRATAMIENTO ACNE ")
	if acumulador_tensor >= acumulador_higiene_profunda and acumulador_tensor >= acumulador_acne  and acumulador_tensor >= acumulador_revitalizante:
		print(f"El tratamiento con mayor realzacion es: TRATAMIENTO TENSOR CON APARATLOGIA ")
	else:
		print(f" El tratamiento con mayor realizacion es: TRATAMIENTO REVITALIZANTE")
def main() ->None:
	tratamientos: list(list) = [['HIGIENE PROFUNDA',1500],
	                            ['TRATAMIENTO ACNE',1500],
	                            ['TRATAMIENTO TENSOR CON APARATOLOGIA',1800],
	                            ['TRATAMIENTO REVITALIZANTE',3000]]
	pacientes: list(list) = []
	salir: str = '6'
	respuesta_usuario: str = input("\n QUE OPCION DESEA REALIZAR?:"
	                               "\n 1. INGRESAR PACIENTE"
	                               "\n 2. MOSTRAR TRATAMIENTO MAS SOLICITADO POR PACIENTES"
	                               "\n 3. MOSTRAR TOTAL DE TRATAMIENTOS VENDIDOS"
	                               "\n 4. MOSTAR PACIENTES NUEVOS Y VIEJOS"
	                               "\n 5. TRATAMIENTO REALIZADO POR PACIENTES NUEVOS"
	                               "\n 6. SALIR \n")

	while respuesta_usuario != salir:
		if respuesta_usuario == '1':
			pacientes = ingresar_paciente(pacientes)
		if respuesta_usuario == '2':
			mostrar_tratamiento_mas_solicitado(pacientes)
		if respuesta_usuario == '3':

		if respuesta_usuario == '4':
			mostrar_cursos_con_asistentes(cursos)
		if respuesta_usuario == '5':

		respuesta_usuario: str = input("\n QUE OPCION DESEA REALIZAR?:"
		                               "\n 1. INGRESAR PACIENTE"
		                               "\n 2. MOSTRAR TRATAMIENTO MAS SOLICITADO POR PACIENTES"
		                               "\n 3. MOSTRAR TOTAL DE TRATAMIENTOS VENDIDOS"
		                               "\n 4. MOSTAR PACIENTES NUEVOS Y VIEJOS"
		                               "\n 5. TRATAMIENTO REALIZADO POR PACIENTES NUEVOS"
		                               "\n 6. SALIR \n")

	if respuesta_usuario == '6':
		print(f"Se va a cerrar el programa")