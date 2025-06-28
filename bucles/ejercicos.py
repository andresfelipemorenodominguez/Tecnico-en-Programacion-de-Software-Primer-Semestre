# total = 0
# numero = int(input("Ingresa un número entero (0 para terminar): "))

# while numero != 0:
#     total += numero
#     numero = int(input("Ingresa otro número entero (0 para terminar): "))

# print(f"La suma total es: {total}")

# contraseña = input("Ingresa la contraseña: ") 

# while contraseña != "python123":
#     print("Contraseña incorrecta")
#     contraseña = input("Intenta denuevo: ")
# print("Contraseña correcta")

# productos = []
# while True:
#     producto = input("Ingresa un producto: ")
#     if producto.lower() == "fin":
#         break
#     else:
#         productos.append(producto)
# print(productos)

# numero = int(input("ingrese un numero: "))
# while numero <= 10:
#     if numero %2 == 0:
#         print(f"{numero}, es par")
#     else:
#         print(f"{numero}, es impar")
#     numero += 1

# notas = []

# while True:
#     entrada = input("Introduce una nota entre 0 y 5 (o 'salir' para terminar): ")
#     if entrada.lower() == "salir":
#         break
#     try:
#         nota = float(entrada)
#         if 0 <= nota <= 5:
#             notas.append(nota)
#         else:
#             print("La nota debe estar entre 0 y 5.")
#     except ValueError:
#         print("Entrada no válida. Por favor, introduce un número o 'salir'.")

# if notas:
#     promedio = sum(notas) / len(notas)
#     print(f"El promedio de las notas es: {promedio:.2f}")
# else:
#     print("No se ingresaron notas válidas.")

# numero = int(input("Ingresa un numero para generar la tabla de multiplicar: "))
# contador = 1

# while contador <= 10:
#     resultado = numero * contador
#     print(f"{numero} * {contador} = {resultado}\n")
#     contador += 1

# numero1 = int(input("Adivina el numero: "))
# numero = 17
# while True:
#     if numero1 < numero:
#         print("el numero es mayor")
#         numero1 = int(input("intenta de nuevo: "))
#     elif numero1 > numero:
#         print("el numero es menor")
#         numero1 = int(input("intenta de nuevo: "))
#     if numero1 == numero:
#         print("numero adivinado!")
#         break

# tupla = ("manzana", "pera", "lulo")
# usuario = input("Adivina la fruta que esta en la tupla: ")

# while True:
#     if usuario not in tupla:
#         print("la fruta que ingresaste no esta en la tupla")
#         usuario = input("Intenta denuevo: ")
#     else:
#         print("la fruta que ingresaste si esta en la tupla!")
#         break

# diccionario = {"hola": "hello", "adios": "goodbye", "uno": "one", "amor": "love", "imprimir": "print"} 
# usuario = input("ingresa una palabra en español para ver su traduccion: ")

# while True:
#     if usuario not in diccionario:
#         print("esta palabra no esta")
#         usuario = input("ingresa otra palabra: ")
#     else:
#         print(f"{usuario} y su traduccion es: {diccionario[usuario]}")

#         break
# print("Escribe sumar = suma, restar = resta, dividir = division, multiplicar = multiplicacion")
# while True:
#     escoger = input("ingrese que operacion matematica desea realizar (o ingrese salir para terminar): ")
#     if escoger.lower() == "sumar":
#         num1 = int(input("Ingresa el primer numero: "))
#         num2 = int(input("Ingresa el segundo numero: "))
#         suma = num1 + num2
#         print(f"el resultado de la suma entre {num1} y {num2} es {suma}")
        
#     elif escoger.lower() == "restar":
#         num1 = int(input("Ingresa el primer numero: "))
#         num2 = int(input("Ingresa el segundo numero: "))
#         resta = num1 - num2
#         print(f"el resultado de la resta entre {num1} y {num2} es {resta}")
        
#     elif escoger.lower() == "dividir":
#         num1 = int(input("Ingresa el primer numero: "))
#         num2 = int(input("Ingresa el segundo numero: "))
#         div = num1 - num2
#         print(f"el resultado de la division entre {num1} y {num2} es {div}")
        
#     elif escoger.lower() == "multiplicar":
#         num1 = int(input("Ingresa el primer numero: "))
#         num2 = int(input("Ingresa el segundo numero: "))
#         mul = num1 - num2
#         print(f"el resultado de la multiplicacion entre {num1} y {num2} es {mul}")
        
#     if escoger.lower() == "salir":
#         break

#     else:
#         print("el valor que ingresaste no es valido")

# datos = {}
# while True:
#     nombre = input("ingresa un nombre: ")
#     if nombre.lower() == "salir":
#         break
#     edad = int(input("ingresa la edad: "))
#     datos[nombre] = edad
# print(datos)

# lista = ["azul", "verde", "rojo", "naranja", "amarillo"]
# while True:
#     usuario = input("intenta adivinar un color que este en la lista: ")
#     if usuario.lower() not in lista:
#         print("el color que usted ingreso no esta en la lista.")
#         usuario = input("intenta de nuevo: ")
#     else:
#         print("felicidades, usted logro acertar!")
#         break

# num = int(input("ingresa un numero: "))
# contador = 1

# while contador <= 5:
#     potencia = num ** contador
#     print(f"{num} ^ {contador} = {potencia}\n: ")
#     contador += 1

# while True:
#     num1 = int(input("ingresa el primer numero: "))
#     num2 = int(input("ingresa el segundo numero: "))
#     num3 = int(input("ingresa el tercer numero: "))
#     num4 = int(input("ingresa el cuarto numero: "))
#     num5 = int(input("ingresa el quinto numero: "))

#     lista = [num1**2, num2**2, num3**2, num4**2, num5**2]
#     break
# print(lista)
dic = {}
while True:
    nombre = input("ingresa tu nombre: ")

    if nombre.lower() == "fin":
        break
    notaf = float(input("ingresa tu nota final: "))
    dic[nombre] = notaf
print(dic)


