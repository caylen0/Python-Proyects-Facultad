"""Crear una función llamada convertir que reciba como parámetro una lista que contiene palabras y devuelva un
diccionario donde se distribuyen las palabras según la inicial y se ordenan alfabéticamente dentro de su inicial.
Ejemplo: Si se invoca la función y se le pasa la siguiente lista: [‘casa’,’auto’,’amor’,’clavel’,’borrar’,’alce’]
Debe devolver: {‘a’:[alce,amor,auto], ‘b’:[borrar], ‘c’:[casa,clavel]}
Ejemplifique con un programa donde se invoque la función desde la funcion main """



def convertir(lista: list) -> dict:
	diccionario: dict = {}
	for palabra in lista:
		if palabra[0] in diccionario:
			diccionario[palabra[0]].append(palabra)
			sorted(diccionario[palabra[0]])
		else:
			diccionario[palabra[0]] = [palabra]
	return sorted(diccionario.items())


def main() -> None:
	lista: list = ['casa', 'auto', 'amor', 'clavel', 'borrar', 'alce' ]
	diccionario_convertido: dict = convertir(lista)
	print(f" La lista de palabras es: {lista}")
	print(f"El diccionario es: {diccionario_convertido}")

main()