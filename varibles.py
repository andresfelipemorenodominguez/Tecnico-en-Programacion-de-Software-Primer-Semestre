"""# Calculadora de Multiplicacion
num1 = int(input("inserta un numero: "))
print(num1)
num2 = int(input("inserta un numero: "))
print(num2)
num3 = num1 * num2
print("el resultado de la multiplicacion es:", num3)

# Promedio de notas
nota1 = float(input("ingrase la primer nota: "))
nota2 = float(input("ingrase la segunda nota: "))
nota3 = float(input("ingrase la tercer nota: "))
nota4 = float(input("ingrase la cuarta nota: "))
suma = nota1 + nota2 + nota3 + nota4 / 4
print("el promedio de las cuatro notas es de: ",suma)

#Potenciacion
b1 = int(input("ingrese la base: "))
ex1 = int(input("ingrese el exponente: "))
re = b1 ** ex1
print("el resultado de la potenciacion es: ",re) 

num1 = int(input("ingrese una base: "))
num2 = int(input("ingrese una base: "))
num3 = int(input("ingrese una exponente: "))
num4 = int(input("ingrese una exponente: "))
op1 = num1 ** num3
op2 = num2 ** num4
result = op1 * op2
print(f"el resultado de la multiplicacion entre la potenciacion: ", op1, "y la potenciacion: ",op2, "es: ", result)

texto = "python"
print(texto[0])

palabra = "python"
len(palabra)"""

b1 = int(input("ingrese la base: "))
ex1 = int(input("ingrese el exponente: "))

if ex1 == 0:
    if b1 == 0:
        print("0 elevado a la 0 es generalmente considerado 1 o indefinido.")
        re = 1
    else:
        print("El exponente es 0.")
        re = 1
    print("El resultado de la potenciacion es: ", re)
elif b1 == 0:
    if ex1 > 0:
        print("La base es 0 y el exponente es positivo.")
        re = 0
        print("El resultado de la potenciacion es: ", re)
    else:
        print("La base es 0 y el exponente es negativo. Esto resulta en division por cero.")
else:
    print("Calculando la potenciacion normal.")
    re = b1 ** ex1
    print("El resultado de la potenciacion es: ", re)




