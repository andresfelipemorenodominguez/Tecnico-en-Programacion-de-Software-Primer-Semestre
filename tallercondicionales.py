#1
# print("Aprobacion de creditos")
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print(f"usted tiene {edad} años, puede solicitar el crédito")
#     cantidad = int(input("Ingrese la cantidad de dinero que desea solicitar: "))
#     if cantidad <= 2500000:
#         print(f"Su crédito por {cantidad} ha sido aprobado")
#     else:
#         print(f"Lo sentimos, su crédito por {cantidad} no ha sido aprobado")
# else:
#     print(f"Lo sentimos, {nombre}, usted tiene {edad} años y no puede solicitar el crédito")
#     print("Debe ser mayor de edad para solicitar un crédito")
#2
print("Cobro de entrada según edades")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 4:
    print("La entrada es gratis")
elif edad >= 5 and edad <= 18:
    print("La entrada cuesta 5 euros")
else:
    print("La entrada cuesta 18 euros")
#3

