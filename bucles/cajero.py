print("_____Cajero_Automatico_____\n")
print("_____Primero Iniciemos Creando una Cuenta_____\n")

escoger = int(input("Ingresa 2 para crear una cuenta nueva: "))

if escoger == 2:
    usuario = input("Ingrese su nombre de usuario: ")
    edad = int(input("Ingrese su edad por favor: "))
    while edad < 18:
        print("usted no puede acceder porque es menor de edad.")
        edad = int(input("intenta denuevo: "))
    contraseña = input("Ingrese una contraseña segura: ")

print("_____Inicia sesion_____\n")
dato1 = input("Ingresa tu nombre de usuario: ")
if dato1 == usuario:
    dato2 = input("Ingresa su contraseña: ")
    if dato2 == contraseña:
        print("Felicidades!, usted ha logrado iniciar sesion con exito.")

        menu = int(input("ahora que desea realizar, (escriba 1 = ver saldo, 2 = retirar saldo, 3 = validar saldo, 4 = salir): "))
        saldo_inicial = 1000
        while True:
            if menu == 1:
                print(f"usted eligio ver el saldo, su saldo actual es: {saldo_inicial}.")#dddddd
                menu = int(input("ahora que desea realizar, (escriba 1 = ver saldo, 2 = retirar saldo, 3 = validar saldo, 4 = salir): "))
            if menu == 2:
                res = int(input("usted eligio retirar saldo, ahora ingrese la cantidad de saldo a retirar: "))
                saldo_inicial -= res
                print(f"usted retiro: {res} y su saldo quedo: {saldo_inicial}")
                if res > saldo_inicial:
                    print("la cantidad que usted ingreso es mayor al saldo inicial")
            menu = int(input("ahora que desea realizar, (escriba 1 = ver saldo, 2 = retirar saldo, 3 = validar saldo, 4 = salir): "))

            if menu == 3:
                sum = int(input("usted eligio validar saldo, ahora ingrese la cantidad que quiere ingresar: "))
                saldo_inicial += sum
                print(f"usted ingreso {sum}, por lo tanto su saldo que asi: {saldo_inicial}")
                menu = int(input("ahora que desea realizar, (escriba 1 = ver saldo, 2 = retirar saldo, 3 = validar saldo, 4 = salir): "))
            
            if menu == 4:
                print("hasta luego que tenga un buen dia")
                break