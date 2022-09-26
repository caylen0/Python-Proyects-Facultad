



def ingresar_propiedad(propiedades: dict) -> dict:
	codigo_propiedad: str = input("\n INGRESE EL CODIGO DE LA PROPIEDAD: ")
	localidad: str = input("\n INGRESE LA LOCALIDAD: ")
	provincia: str = input("\n INGRESE LA PROVINCIA: ")
	metros_cuadrados: int = int(input("\n INGRESE LOS METROS CUADRADOS: "))
	ambietes: int = int(input("\n INGRESE LA CANTIDAD DE AMBIENTES:"))
	comodidades: list = []
	ingresar_comodidad: str = input("\n INGRESE LA COMODIDAD: ")
	comodidades.append(ingresar_comodidad)
	ingresar_comodidades: str = input("\n Desea agregar otra comodidad? SI/NO: ").upper()
	while ingresar_comodidades == 'SI':
		ingresar_comodidad: str = input("\n INGRESE LA COMODIDAD: ")
		comodidades.append(ingresar_comodidad)
		ingresar_comodidades: str = input("\n Desea agregar otra comodidad? SI/NO: ").upper()
	valor: int = int(input("\n INGRESE EL VALOR DE LA PROPIEDAD:"))
	propiedades[codigo_propiedad] = [localidad, provincia, metros_cuadrados, ambietes, comodidades, valor]
	return propiedades


def mostrar_propiedad_por_comodidad(comodidad: str, propiedades: dict) -> None:
	propiedades_con_comodidad: list[tuple] = []
	for propiedad in propiedades:
		comodidades: list = propiedades[propiedad][4]
		if comodidad in comodidades:
			propiedades_con_comodidad.append((propiedades[propiedad][1], propiedades[propiedad][5]))
	print(sorted(propiedades_con_comodidad))


def mostrar_top_3_mayor_valor_por_ambiente(propiedades: dict) -> None:
	provincias_con_valor_por_ambiente: dict[list] = {}
	for propiedad in propiedades:
		provincia: str = propiedades[propiedad][1]
		valor: int = propiedades[propiedad][5]
		ambientes: int = propiedades[propiedad][3]
		if provincia in provincias_con_valor_por_ambiente:
			provincias_con_valor_por_ambiente[provincia][0] = provincias_con_valor_por_ambiente[provincia][0] + valor
			provincias_con_valor_por_ambiente[provincia][1] = provincias_con_valor_por_ambiente[provincia][1] + ambientes
			provincias_con_valor_por_ambiente[provincia][2] += 1
		else:
			provincias_con_valor_por_ambiente[provincia] = [valor, ambientes, 1]

	for provincia in provincias_con_valor_por_ambiente:
		print(f"La provincia es: {provincia}")
		print(f"El valor promedio por ambiente es: ${provincias_con_valor_por_ambiente[provincia][0] / provincias_con_valor_por_ambiente[provincia][1]}")
		print(f"cantidad de propiedades en portfolio es: {provincias_con_valor_por_ambiente[provincia][2]}")

def mostar_reporte_comodidades_disponibles(propiedades: dict) -> None:
	comodidades: dict = {}
	lista_comodidades: list = []
	for propiedad in propiedades:
		lista_comodidades = propiedades[propiedad][4]
		for comodidad in lista_comodidades:
			if comodidad in comodidades:
				comodidades[comodidad] += 1
			else:
				comodidades[comodidad] = 1
	for comodidad in comodidades:
		print(f"\n La comodidad es: {comodidad} y aparecio {comodidades[comodidad]} veces")

def mostrar_localidades_con_mas_de_la_mitad_con_cinco_ambientes(propiedades: dict) -> None:
	localidades_con_cinco_ambientes: dict[list] = {}
	for propiedad in propiedades:
		localidad: str = propiedades[propiedad][0]
		ambientes: int = propiedades[propiedad][3]
		valor: int = propiedades[propiedad][5]
		if localidad in localidades_con_cinco_ambientes and ambientes > 5:
			localidades_con_cinco_ambientes[localidad][0] += 1 #cantidad de localidades con 5 ambientes
			localidades_con_cinco_ambientes[localidad][1] += 1 #cantidad total
			localidades_con_cinco_ambientes[localidad][2] += valor #valor
		elif localidad in localidades_con_cinco_ambientes and ambientes <= 5:
			localidades_con_cinco_ambientes[localidad][1] += 1
		else:
			if ambientes > 5:
				localidades_con_cinco_ambientes[localidad] = [1, 1, valor]
			else:
				localidades_con_cinco_ambientes[localidad] = [0, 1, 0]

	for localidad in localidades_con_cinco_ambientes:
		porcentaje = localidades_con_cinco_ambientes[localidad][0]/localidades_con_cinco_ambientes[localidad][1]
		if (porcentaje >= 0.5): #porque enunciado pide msotrar localidad con mas de 50 porciento de propiedades con mas de 5 ambientes
			print(f"La localidad es: {localidad}")
			print(f"el porcentaje es: {porcentaje}")
			print(f"El promedio de localidad con mas de 50% de localidades con mas de 5 ambientes es: {localidades_con_cinco_ambientes[localidad][2]}")

def main() -> None:
	propiedades: dict = {'FC327': ['mina clavero', 'cordoba', 1027, 6, ['pileta', 'parrilla', 'quincho'], 250000],
	                     'FC328': ['mina clavero', 'buenos aires', 1027, 6, ['pileta', 'parrilla', 'quincho'], 200000],
	                     'FC329': ['mina clavero', 'buenos aires', 1027, 6, ['pileta', 'parrilla', 'quincho'], 180000]
	                     }
	# { (codigo,[localidad,provincia,metros cuadrados,ambientes,[comodidades],valor])

	salir: str = "6"
	respuesta_usuario: str = input("\n QUE DESEA REALIZAR?:"
	                               "\n 1. INGRESAR PROPIEDAD "
	                               "\n 2. BUSCAR PROPIEDADES SEGUN COMODIDAD"
	                               "\n 3. TOP 3 DE PROVINCIAS CON MAYOR PROMEDIO POR AMBIENTE "
	                               "\n 4. MOSTRAR REPORTE DE TODAS LAS COMODIDADES DISPONIBLES"
	                               "\n 5. MOSTRAR LOCALIDADES DONDE EL % DE PROPIEDADES PUBLICADAS CON MAS DE 5 AMBIENTES SEA MAYOR AL 50%"
	                               "\n 6. SALIR \n")
	while respuesta_usuario != salir:
		if respuesta_usuario == "1":
			propiedades = ingresar_propiedad(propiedades)
		if respuesta_usuario == '2':
			respuesta: str = input("\n INGRESE LA COMODIDAD QUE DESEA BUSCAR: ")
			mostrar_propiedad_por_comodidad(respuesta, propiedades)
		if respuesta_usuario == '3':
			mostrar_top_3_mayor_valor_por_ambiente(propiedades)
		if respuesta_usuario == '4':
			mostar_reporte_comodidades_disponibles(propiedades)
		if respuesta_usuario == '5':
			mostrar_localidades_con_mas_de_la_mitad_con_cinco_ambientes(propiedades)
		respuesta_usuario: str = input("\n QUE DESEA REALIZAR?:"
			                               "\n 1. INGRESAR PROPIEDAD "
			                               "\n 2. BUSCAR PROPIEDADES SEGUN COMODIDAD"
			                               "\n 3. TOP 3 DE PROVINCIAS CON MAYOR PROMEDIO POR AMBIENTE "
			                               "\n 4.  MOSTRAR REPORTE DE TODAS LAS COMODIDADES DISPONIBLES"
			                               "\n 5. MOSTRAR LOCALIDADES DONDE EL % DE PROPIEDADES PUBLICADAS CON MAS DE 5 AMBIENTES SEA MAYOR AL 50%"
			                               "\n 6. SALIR \n")
	if respuesta_usuario == '6':
		print(f"\n EL PROGRAMA SE VA A CERRAR")

main()

