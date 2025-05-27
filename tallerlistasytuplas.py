#solicita 10 numeros al usuario usando input y los convierte a enteros usando int()
#crea una lista con esos numreros
#crea una tupla por cada numero, donde cada tupla contiene el numero y su cuadrado
#agrupa esas tuplas en otra lista
#realiza operaciones matematicas
#suma total de los 10 numeros
#promedio de los numeros
#doble de la suma
#mitad de promedio
#una lista de operaciones matematicas entre algunos numeros de la lista (sumas, restas, multiplicaciones y divisiones)

num1 = int(input("Ingrese el 1ER número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))
num6 = int(input("Ingrese el sexto número: "))
num7 = int(input("Ingrese el séptimo número: "))
num8 = int(input("Ingrese el octavo número: "))
num9 = int(input("Ingrese el noveno número: "))
num10 = int(input("Ingrese el décimo número: "))    
# Crear una lista con los números ingresados
numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
print(f"la lista de los 10 numeros es: {numeros}")
#tuplas que contienen el numero y su cuadrado
tupla1 = (num1, num1**2)
tupla2 = (num2, num2**2)
tupla3 = (num3, num3**2)
tupla4 = (num4, num4**2)
tupla5 = (num5, num5**2)
tupla6 = (num6, num6**2)
tupla7 = (num7, num7**2)
tupla8 = (num8, num8**2)
tupla9 = (num9, num9**2)
tupla10 = (num10, num10**2)
#agrupar las tuplas en una lista
lista_tuplas = [tupla1, tupla2, tupla3, tupla4, tupla5, tupla6, tupla7, tupla8, tupla9, tupla10]
print(f"la lista que contiene las tuplas es: {lista_tuplas}")
#operaciones matematicas
suma = sum(numeros)
promedio = suma / len(numeros)
doble_suma = suma * 2
mitad_promedio = promedio / 2
print(f"la suma total de los 10 numeros es de: {suma}")
print(f"el promedio de los numeros es de: {promedio}")
print(f"el doble de la suma es de: {doble_suma}")
print(f"la mitad del promedio es de: {mitad_promedio}")

lista_operaciones = [(num1 + num2), (num3 - num4), (num5 * num6), (num7 / num8)]
print(f"el resultado de las operaciones es: {lista_operaciones}")