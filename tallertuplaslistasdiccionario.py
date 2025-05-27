#1
# producto = input("ingrese el nombre del profucto: ")
# precio = float(input("ingrese el precio unitario del producto: "))
# cantidad = int(input("ingrese la cantodad que quiere perdir: "))
# tupla = (producto, precio)
# print(tupla)
# lista = [tupla, cantidad]
# print(lista)
# diccionario = {"producto": lista}
# print(diccionario)
# total = precio * cantidad
# print(f"el costo total es de: {total}")

#2
# producto1 = input("ingrese el nombre del profucto: ")
# precio1 = float(input("ingrese el precio unitario del priducto: "))
# cantidad1 = int(input("ingrese la cantodad que desea pedir: "))
# #2
# producto2 = input("ingrese el nombre del profucto: ")
# precio2 = float(input("ingrese el precio unitario del priducto: "))
# cantidad2 = int(input("ingrese la cantodad que desea pedir: "))
# #3
# producto3 = input("ingrese el nombre del profucto: ")
# precio3 = float(input("ingrese el precio unitario del priducto: "))
# cantidad3 = int(input("ingrese la cantodad que desea pedir: "))
# #tuplas
# tupla1 = (producto1, precio1, cantidad1)
# tupla2 = (producto2, precio2, cantidad2)
# tupla3 = (producto3, precio3, cantidad3)
# #listas
# lista1 = [tupla1, cantidad1]
# lista2 = [tupla2, cantidad2]
# lista3 = [tupla3, cantidad3]
# #diccionario
# diccionario = {"producto1": producto1, "producto2": producto2, "producto3": producto3}
# totalp1 = precio1 * cantidad1
# totalp2 = precio2 * cantidad2
# totalp3 = precio3 * cantidad3
# print(f"usted compro una cantidad de: {cantidad1} {producto1} con un precio de: {precio1} por lo tanto el costo total es: {totalp1}.")
# print(f"usted compro una cantidad de: {cantidad2} {producto2} con un precio de: {precio2} por lo tanto el costo total es: {totalp2}.")
# print(f"usted compro una cantidad de: {cantidad3} {producto3} con un precio de: {precio3} por lo tanto el costo total es: {totalp3}.")

#3

nombre = input("ingrese el nombre del estudiante: ")

asig1 = input("ingrese la 1er asignatura que cursa el estudiante: ")
asig2 = input("ingrese la 2da asignatura que cursa el estudiante: ")
asig3 = input("ingrese la 3er asignatura que cursa el estudiante: ")


print(asig1.upper())
nota1 = float(input(f"ingrese la 1er nota de {asig1}: "))
nota2 = float(input(f"ingrese la 2da nota de {asig1}: "))
print(asig2.upper())
nota3 = float(input(f"ingrese la 1er nota de {asig2}: "))
nota4 = float(input(f"ingrese la 2da nota de {asig2}: "))
print(asig3.upper())
nota5 = float(input(f"ingrese la 1er nota de {asig3}: "))
nota6 = float(input(f"ingrese la 2da nota de {asig3}: "))

promedio1 = nota1 + nota2 / 2
promedio2 = nota3 + nota4 / 2
promedio3 = nota5 + nota6 / 2

tupla1 = (asig1, promedio1)
tupla2 = (asig2, promedio1)
tupla3 = (asig3, promedio3)

lista1 = [tupla1, nota1, nota2]
lista2 = [tupla2, nota3, nota4]
lista3 = [tupla3, nota5, nota6]

lista4 = [asig1, asig2, asig3]

diccionario = {"nombre": nombre, "materias": lista4,}

promedio_final = promedio1 + promedio2 + promedio3 / 3

print(f"el estudiante {nombre} en la materia de {asig1} ha sacado como promedio {promedio1}, en la meteria de {asig2} ha sacado como promedio {promedio2}, y en la materia de {asig3} ha sacado {promedio3} por lo tanto su nota final es de: {promedio_final}")
