# 🌀 Documentación: Bucles `while` y `while True` en Python

# 📘 ¿Qué es un bucle `while`?
# Un bucle `while` se utiliza para repetir un bloque de código mientras se cumpla una condición determinada.

# 🔧 Sintaxis básica de `while`
# while condición:
#     # código a ejecutar mientras la condición sea verdadera

# ✅ Ejemplo:
contador = 1
while contador <= 5:
    print("Repetición número", contador)
    contador += 1

print("-----")

# 🔁 ¿Qué es `while True`?
# Un bucle `while True` es un bucle infinito, ya que la condición siempre es True.

# 🔧 Sintaxis de `while True`
# while True:
#     # código que se repite indefinidamente

# ✅ Ejemplo con `break`:
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        print("Has salido del bucle.")
        break
    print("Escribiste:", entrada)

# 🛑 ¿Cómo se detiene un bucle?
# - Usando break
# - Haciendo que la condición sea False

# ⚠️ Errores comunes
# - Olvidar actualizar la condición → bucles infinitos no deseados
# - No usar break en while True cuando sea necesario

# 📌 Cuándo usar cada uno:
# - while → cuando conoces la condición de salida
# - while True → cuando necesitas un bucle indefinido controlado desde dentro

# 🧠 Ejercicio práctico:
numero = 0
while numero < 3:
    print("Número:", numero)
    numero += 1

while True:
    respuesta = input("¿Quieres continuar? (s/n): ")
    if respuesta.lower() == "n":
        print("Hasta luego")
        break
