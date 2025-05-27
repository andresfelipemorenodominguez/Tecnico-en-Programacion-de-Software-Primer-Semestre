print("Bienvenido al sistema de calificaciones")
print("ingrese su nombre y acontinuacion ingrese que asignaturas desea promediar, despues se le pedira las notas de las materias y se le mostrara el promedio de cada materia y el promedio general")

nombre = input("ingrese su nombre: ")

#materia1

materia1 = input("ingrese la primer materia: ")
print(f"La asignatura seleccionada es: {materia1}")
nota1 = float(input(f"ingrese 1er nota de {materia1}: "))
nota2 = float(input(f"ingrese 2da nota de {materia1}: "))
nota3 = float(input(f"ingrese 3er nota de {materia1}: "))
promedio1 = (nota1 + nota2 + nota3) / 3
print(f"el promedio de {materia1} es: {promedio1}")

#materia2

materia2 = input("ingrese la segunda materia: ")
print(f"La materia seleccionada es: {materia2}")
nota1 = float(input(f"ingrese 1er nota de {materia2}: "))
nota2 = float(input(f"ingrese 2da nota de {materia2}: "))
nota3 = float(input(f"ingrese 3er nota de {materia2}: "))
promedio2 = (nota1 + nota2 + nota3) / 3
print(f"el promedio de {materia2} es: {promedio2}")

#materia3

materia3 = input("ingrese la tercer materia: ")
print(f"La materia seleccionada es: {materia3}")
nota1 = float(input(f"ingrese 1er nota de {materia3}: "))
nota2 = float(input(f"ingrese 2da nota de {materia3}: "))
nota3 = float(input(f"ingrese 3er nota de {materia3}: "))
promedio3 = (nota1 + nota2 + nota3) / 3
print(f"el promedio de {materia3} es: {promedio3}")

#materia4

materia4 = input("ingrese la cuarta materia: ")
print(f"La materia seleccionada es: {materia4}")
nota1 = float(input(f"ingrese 1er nota de {materia4}: "))
nota2 = float(input(f"ingrese 2da nota de {materia4}: "))
nota3 = float(input(f"ingrese 3er nota de {materia4}: "))
promedio4 = (nota1 + nota2 + nota3) / 3
print(f"el promedio de {materia4} es: {promedio4}")

#materia5

materia5 = input("ingrese la quinta materia: ")
print(f"La materia seleccionada es: {materia5}")
nota1 = float(input(f"ingrese 1er nota de {materia5}: "))
nota2 = float(input(f"ingrese 2da nota de {materia5}: "))
nota3 = float(input(f"ingrese 3er nota de {materia5}: "))
promedio5 = (nota1 + nota2 + nota3) / 3
print(f"el promedio de {materia5} es: {promedio5}")

#promedio general

promedio_general = (promedio1 + promedio2 + promedio3 + promedio4 + promedio5) / 5
print(f"el promedio general del estudiante {nombre} es: {promedio_general}")
