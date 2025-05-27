"""
Listas en Python
Una lista en Python es una estructura de datos que se utiliza para almacenar multiples elementos en una
sola variable. Es uno de los tipos de datos mas utilizados en Python ya que es mutable, lo que significa 
que puede cambiar sus elementos despues de haberlos creado."""


#Ejemplo de una lista en Python
mi_lista = [1, 2, 3, 4, 5]

#Lista Vacia
mi_lista_vacia = []

#Lista con diferentes tipos de datos
mi_lista_diferentes_tipos = [1, "hola", 3.14, True]

#1 es un numero entero (int)
#"hola" es una cadena de texto (string)
#3.14 es un numero decimal (float)
#True es un valor booleano (boolean)

#Acceder a un elemento de la lista
print(mi_lista[0]) # 1 Imprime el primer elemento de la lista
print(mi_lista[-1])# 2 Imprime el ultimo elemento de la lista

#Modificar un elemento de la lista
mi_lista[1] = "hola" # Cambia el segundo elemento de la lista a "hola"
print(mi_lista) # [1, "hola", 3, 4, 5]

#Metodos comunes de listas

#Agregar un elemento a la lista .append()
mi_lista.append(6) # Agrega el elemento 6 al final de la lista
print(mi_lista) # [1, "hola", 3, 4, 5, 6]

#Agregar varios elementos a la lista .extend()
mi_lista.extend([7, 8, 9]) # Agrega los elementos 7, 8 y 9 al final de la lista
print(mi_lista) # [1, "hola", 3, 4, 5, 6, 7, 8, 9]

#Insertar un elemento en una posicion especifica .insert()
mi_lista.insert(0, "hola") # Inserta el elemento "hola" en la posicion 0 de la lista
print(mi_lista) # ["hola", 1, "hola", 3, 4, 5, 6, 7, 8, 9]

#Eliminar un elemento de la lista .remove()
mi_lista.remove(1) # Elimina el elemento 1 de la lista
print(mi_lista) # ["hola", "hola", 3, 4, 5, 6, 7, 8, 9]

#Eliminar el ultimo elemento de la lista .pop()
mi_lista.pop() # Elimina el ultimo elemento de la lista
print(mi_lista) # ["hola", "hola", 3, 4, 5, 6, 7, 8]

#Eliminar un elemento de una posicion especifica .pop()
mi_lista.pop(0) # Elimina el elemento en la posicion 0 de la lista
print(mi_lista) # ["hola", 3, 4, 5, 6, 7, 8]

#Indexar un elemento de la lista .index()
print(mi_lista.index("hola")) # 1 Imprime la posicion del elemento "hola" en la lista

#Ordenar una lista .sort() / sorted()
mi_lista2 = [3, 9, 7, 5, 6, 8, 4]
mi_lista2.sort() # Ordena la lista de menor a mayor
print(mi_lista2) # [3, 4, 5, 6, 7, 8, 9]

#Copiar una lista .copy()
mi_lista3 = mi_lista2.copy() # Copia la lista mi_lista2 en la lista mi_lista3
print(mi_lista3) # [3, 4, 5, 6, 7, 8, 9]

#Eliminar una lista .clear()
mi_lista3.clear() # Elimina todos los elementos de la lista
print(mi_lista3) # []

#Ejemplos de listas avanzadas

# print("Suma numeros")
# numeros = [int(input("ingrese un numero: ")), int(input("ingrese un numero: "))]
# suma = numeros[0] + numeros[1]
# print("La suma de los numeros es: ", suma)

# print("cambiar un dato de una lista")

# materia = ["matematicas", "fisica", "quimica", "historia", "lengua"]
# print(materia)
# materia[0] = "ingles"
# print(materia)

#Ejercicios de listas avanzadas con metodo .append()

#1
# productos = []
# print(productos)
# print("Ingrese 3 productos")
# productos.append(input("Ingrese un producto: "))
# productos.append(input("Ingrese un producto: "))
# productos.append(input("Ingrese un producto: "))
# print(productos)

#2
# print("precio de 3 articulos")
# precios = []
# precios.append(float(input("Ingrese el precio del primer articulo: ")))
# precios.append(float(input("Ingrese el precio del segundo articulo: ")))
# precios.append((float("Ingrese el precio del tercer articulo: ")))
# op = precios[0] + precios[1] + precios[2]
# print(f"el resultado de la suma de los precios de los tres articulos es de: {op}")

#3
# numeros = []
# numeros.append(int(input("ingrese el 1er numero: ")))
# numeros.append(int(input("ingrese el 2do numero: ")))
# numeros.append(int(input("ingrese el 3er numero: ")))
# numeros.append(int(input("ingrese el 4to numero: ")))
# print(f"el numero mayor de la lista {numeros} fue: {max(numeros)} y el numero menor fue: {min(numeros)}.")

#Tienes una lista desordenada y desorganizada de nombre de clientes, Debes:
#Agregar un nombre adicional: "JULIANA".
#Encontrar cuantos elementos hay en una lista despues de agragar a juliana.
#Identificar el nombre alfabeticamente mayor a menor.
#Eliminar la primera aparicion del nombre que esta alfabeticamente en el medio entre el menor y el mayor.
#Mostar la posicion (indice) de "JULIANA" despues de la eliminacion.
#Mostrar la lista final resultante.


#Tienes una lista desordenada y desorganizada de nombre de clientes
nombres = ["MARIA", "JUAN", "CARLOS", "MARIANA", "VALERIA", "ESTEBAN", "ANDRES", "GIOVANNI"]
print(nombres)
#Agregar un nombre adicional: "JULIANA".
nombres.append("JULIANA")
print(nombres)
#Encontrar cuantos elementos hay en una lista despues de agragar a juliana.
print(f"en la lista despues de agregar a juliana hay: {len(nombres)}")
#Identificar el nombre alfabeticamente mayor a menor.
print(f"el nombre mayor alfabeticamente es: {max(nombres)} y  el menor alfabeticamentes es: {min(nombres)}")
#Eliminar la primera aparicion del nombre que esta alfabeticamente en el medio entre el menor y el mayor.
ordenada = sorted(nombres)
medio = ordenada[len(ordenada)//2]
print(f"el nombre que esta en el medio alfabeticamente es: {medio}")
print(f"el nombre removido fue: {(medio)}")
nombres.remove(medio)
print(nombres)
#Mostar la posicion (indice) de "JULIANA" despues de la eliminacion.
print(nombres.index("JULIANA"))
print(nombres)


numero = [1,2,3,4]
numero.pop()
print(numero)

