# contador = 1
# while contador <= 100:
#     print("contador", contador)
#     contador -= 1

# contador = int(input("ingresar numero: "))

# while contador > 0:
#     print(f"contador:, {contador}")
#     contador -= 1
#     print("termino el contador")

while True:
    texto = input("Escribe algo (O escribe salir para terminar)")
    if texto == "salir":
        break
    print("Escribiste:", texto)
