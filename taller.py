#1. escribe un programa que pida dos numeros al usuario y muestre su suma

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# suma = num1 + num2
# print("la suma de los dos numeris es de: ", suma)

#2. escribe un programa que pida dos numeros y muestre la resta del primero menos el segundo

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# resta = num1 - num2
# print("la resta de los dos numeros es de: ", resta)

#3. escribe un programa que multiplique dos numeros ingresados por el usuario

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# multiplicacion = num1 * num2
# print("la multiplicacion de los dos numeros es de: ", multiplicacion)

#4. escribe un programa que divida dos numeros ingresados por el usuario

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# division = num1 / num2
# print("la division de los dos numeros es de: ", division)

#4. pide al usuario su nombre y apellido por separado, y muestra un saludo con el nombre completo

# nombre = input("Por favor ingrse su nombre: ")
# apellido = input("Porfavor ingrese su apellido: ")
# print("Hola, ", nombre, apellido, "¿Como estas?")

#6. escribe un programa que pida al usuario su nombre y muestre solo la primera letra

# nombre = input("Por favor ingrese su nombre: ")
# print(nombre[0])

#7. escribe un programa que pida una palabra y muestre su ultima letra

# palabra = input("ingrese una palabra: ")
# print(palabra[-1])

#8. escribe un programa que calcule el area de un rectangulo pidiendo la base y la altura

# base = int(input("ingrese la base del rectangulo: "))
# altura = int(input("ingrese la altura: "))
# print("el area del rectangulo es de:", base * altura)

#9. pide al usuario el año de nacimiento y calcula su edad actual

# año = int(input("ingrese su edad de nacimiento: " ))
# edad = 2025 - año
# print("su edad actual es de: ", edad)

#10. escribe un programa que pida un nombre de usuario y un dominio, y genera una direccion de correo

# usuario = input("ingrse su usuario: ")
# dominio = input("ingrese un dominio: ")
# print(usuario + "@" + dominio)

#11. pide al usuario su nombre y muestra cuantas letras tiene

# nombre = input("ingrese su nombre: ")
# print(len(nombre))

#12. pide dos palabras al usuario y muestra la combinacion de ambas en una sola

# palabra1 = input("ingrese la primer palabra: ")
# palabra2 = input("ingrese la segunda palabra:")
# print(palabra1 + palabra2)

#13. pide una palabra y muestra su segunda letra

# palabra = input("ingrese una palabra: ")
# print(palabra[1]) 

#14. pide una palabra y muestra sus tres primeras letras

# palabra = "python"
# print(palabra[0:3])

#15. pide una palabra y muestra las plabras en orden inverso

# palabra = input("ingrese una palabra: ")
# print(palabra[::-1]) se usa :: para invertir los caracteres de una cadena

#16. pide dos numeros y muestra la suma, la resta, la multiplicacion y la division en diferentes lineas

# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese otro numero: "))
# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2
# print("el resultado de la suma es de:", suma)
# print("el resultado de la resta es de:", resta)
# print("el resultado de la multiplicacion es de:", multiplicacion)
# print("el resultado de la division es de:", division)

#17. pide un numero al usuario y muestra el doble de ese numero

# num1 = int(input("ingrese un numero: "))
# print(num1 * 2)

#18. pide un numero al usuario y muestra la mitad

# num1 = int(input("ingrese un numero: "))
# print(num1 / 2)

#19. pide al usuario una palabra y repitela 3 veces usando concatenacion

# palabra = input("ingrese una palabra: ")
# print(palabra+palabra+palabra)

#20. pide al usuario una frase y muestra cuantos caracteres tiene

# frase = input("ingrese una frase: ")
# print(len(frase))

#21. pide al usuario una palabra y muestra las dos primeras letras y las dos ultimas que tiene

# palabra = input("ingrese una palabra: ")
# print(palabra[0:2] + palabra[-2:])

#22. pide una palabra y muestra la letra del medio(solo si tiene numero impar de letras)

# palabra = input("ingrese una palabra: ")
# print(palabra[len(palabra)//2])

#23. pide una frase y muestra los primeros 10 caracteres

# frase = input("ingrese una frase: ")
# print(frase[0:10])

#24. pide un numero y muestra el resultado de elevarlo al cuadrado(sin usar potencias solo con multiplicacion)

# num1 = int(input("ingrese un numero: "))
# print(num1 * num1)

#25. pide al usuario dos numeros y muestra cual es el mayor (sin usar if solo operaciones)

# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese un numero: "))
# print(max(num1, num2)) max para saber el numero mayor

#26. pide al usuario la edad y muestra cuantos dias ha vivido

# edad = int(input("ingrese su edad: "))
# print(edad * 365)

#27. pide al usuario una palabra y muestra cada letra por separado(una por linea)

# palabra = input("ingrese una palabra: ")

#28. pide una palabra y muestra si tiene mas de 5 letras (usando solo operaciones de longitud y texto)

# palabra = input("ingrese una palabra: ")
# print(len(palabra) > 5) len para saber la longitud de la palabra

#29. pide un numero y muestra el valor multiplicado por 10

# num = int(input("ingrese un numero: "))
# print(num * 10)

#30. pide una palabra y muestra la palabra escrita dos veces, una en mayusculas y la otra en minusculas

palabra = input("ingrese una palabra: ")
print(palabra.upper()) #upper para mayusculas
print(palabra.lower()) #lower para minusculas




