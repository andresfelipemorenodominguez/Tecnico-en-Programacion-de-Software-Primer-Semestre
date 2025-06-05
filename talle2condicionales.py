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

