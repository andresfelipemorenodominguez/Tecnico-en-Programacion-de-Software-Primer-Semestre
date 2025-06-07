#1
# numero = int(input("Ingrese un número: "))
# if numero == 0:
#     print(f"El número {numero} es cero.")
# elif numero < 0:
#     print(f"El número {numero} es negativo.")
# else:
#     print(f"El número {numero} es positivo.")

#2
# num1 = int(input("Ingresa un número: "))
# num2 = int(input("Ingresa otro número: "))

# if num1 < num2:
#     print(f"El número {num1} es menor que {num2}.")
# elif num1 > num2:
#     print(f"El número {num1} es mayor que {num2}.")
# else:
#     print("Ambos números son iguales.")

#3
# num1 = int(input("Ingresa un número: "))

# if num1 %2 == 0:
#     print(f"El número {num1} par")
# else:
#     print(f"El número {num1} impar")

#4
# num1 = int(input("Ingresa un número: "))

# if num1 > 10 and num1 < 20:
#     print(f"El número {num1} esta entre 10 y 20")
# else:
#     print(f"El número {num1} no está entre 10 y 20")

#5
# num1 = int(input("Ingresa un número: "))
# num2 = int(input("Ingresa otro número: "))
# num3 = int(input("Ingresa el ultimo número: "))

# if num1 > num2 and num1 > num3:
#     print(f"el numero {num1} es mayor que {num2} y {num3}.")
# else:
#     print(f"el numero {num1} no es mayor que {num2} y {num3}. ")

#6
# total = float(input("Ingresa el total de la compra: $"))

# if total > 100:
#     descuento = total * 0.10
#     precio_final = total - descuento
#     print(f"Se aplicó un 10% de descuento (${descuento:.2f}).")
# else:
#     precio_final = total
#     print("No se aplicó descuento.")

# print(f"El precio final a pagar es: ${precio_final:.2f}")

#7
# edad = int(input("ingrese su edad para poder votar: "))
# if edad >= 18:
#     print(f"usted tiene {edad}, por lo tanto usted puede votar")
# else:
#     print("usted no tiene la edad suficiente para poder votar")


#8
# precio = int(input("ingrese el precio del producto: "))
# print("ingrese que tipo de cliente es usted, escriba VIP o normal")
# tipo = input("ingrese que tipo de cliente es usted: ")

# if tipo == "VIP":
#     descuento = precio * 0.20
#     preciofn = precio - descuento
#     print(f"como usted es un usuario VIP se le aplica el 20% de descuento, por lo tanto el precio final es de: {preciofn}")
# elif tipo == "normal":
#     print("usted es un usuraio normal, no se le aplican descuentos")

#9
# numero = int(input("Ingrese un número: "))
# if numero % 5 == 0 and numero % 3 == 0:
#     print(f"El número {numero} es múltiplo de 5 y de 3.")
# else:
#     print(f"El número {numero} no es múltiplo de 5 y de 3 al mismo tiempo.")

#10 Dado un número, verifica si es divisible entre dos números dados.
# numero = int(input("Ingrese un número: "))
# divisor1 = int(input("Ingrese el primer divisor: "))
# divisor2 = int(input("Ingrese el segundo divisor: "))
# if numero % divisor1 == 0 and numero % divisor2 == 0:
#     print(f"El número {numero} es divisible entre {divisor1} y {divisor2}.")
# else:
#     print(f"El número {numero} no es divisible entre {divisor1} y {divisor2} al mismo tiempo.")

#11
# lista = [1, 2, 3, 4, 5]
# if 7 in lista: 
#     print("esta en la lista")
# else:
#     print("no esta en la lista")

#12
# lista = [1, 234, 10, 64, 45]
# if lista[2] > 10:
#     print("el tercer numero de la lista es mayor que 10")
# elif lista[2] < 10:
#     print("el tercer numero de la lista no es mayor que 10")
# else:
#     print("el tercer numero de la lista es igual a 10")

#13
# lista = [3, 5, 7, 9]
# sum = lista[0] + lista [2]
# if sum > 10:
#     print("suma alta")
# else:
#     print("suma baja")

#14
# lista = ["Ana", "Luis", "Pedro", "Juan"]
# if lista.pop() == "Marta": #El metodo .pop() devuelve el ultimo valor de la lista
#     print("Nombre correcto")
# else:
#     print("Nombre incorrecto")

#15
# lista = ["Rojo", "Negro", "Amarillo"]
# if lista[1] == "Azul": #Aqui estamos actualizando un dato de una lista
#     lista[1] = "Verde"
#     print(lista)
# else:
#     print("el segundo color no es igual a azul")

#16
# tupla = (20, 8, 12, 30)
# if tupla[0] < tupla[3]:
#     mi_lista = list(tupla)
#     mi_lista.sort()
#     print(mi_lista)
# else:
#     mi_lista = list(tupla)
#     mi_lista.sort(reverse = True) #con el metodo nombre_de_la_lista.sort(reverse = True) podemos hacer que una lista vaya en orden descendiente
#     print(mi_lista)

#17

# tupla = (25, 32, 28)
# if tupla[1] > 30:
#     print("Edad mayor a treinta")
# else:
#     print("edad menor o igual a treinta")

#18
# tupla = (1, 2, 3)
# lista = list(tupla)
# if lista[1] == 2:
#     lista[1] = 10
#     mi_tupla = tuple(lista)
#     print(mi_tupla)
# else:
#     print("el numero no es igual a 2")

#19
# tupla = (4, 9)
# if tupla[1] > 5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")

#20
# tupla1 = (3, 4)
# tupla2 = (3, 5)
# if tupla1 == tupla2:
#     print("tuplas iguales")
# else:
#     print("tuplas diferentes")

#21
# dic = {"nombre": "Juan", "edad": 17}
# if dic["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

#22
# dic = {"nombre": "Lucía", "edad": 20}
# if dic["edad"] > 18:
#     dic["edad"] = 21
#     print(dic)
# else:
#     print("la edad no es mayor a 18")

#23
# dic = {"nombre": "Carlos"}
# if "ciudad" not in dic:
#     dic["ciudad"] = "bogota"
#     print(dic)
# else:
#     print("la clave ciudad existe")

#24
# dic = {"producto": "pan", "precio": 1200}
# if "precio" in dic:
#     print(dic["precio"])
# else:
#     print("No hay precio")

#25
dic = {"pan": 1200, "leche": 2000}
if "pan" in dic:
    print(dic["pan"])
else:
    print("Producto no disponible")
