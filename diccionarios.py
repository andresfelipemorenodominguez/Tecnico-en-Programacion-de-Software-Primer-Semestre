# 📘 Documentación: Diccionarios en Python

# 🧾 ¿Qué es un diccionario?
# Un diccionario es una colección de datos en formato clave: valor.
# Permite almacenar información de forma organizada y fácil de acceder por su clave.

# 🔧 Sintaxis:
# diccionario = { "clave1": valor1, "clave2": valor2 }

# ✅ Ejemplo básico:
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Bogotá"
}
print(persona)

# 🎯 Acceder a un valor:
print("Nombre:", persona["nombre"])

# 🛑 Si la clave no existe y la accedes directamente, dará error:
# print(persona["telefono"])  # Esto genera KeyError

# ✅ Acceso seguro con `.get()`:
print("Teléfono:", persona.get("telefono", "No disponible"))

# ➕ Agregar o modificar elementos:
persona["telefono"] = "123456789"  # Agregar nuevo par
persona["edad"] = 31              # Modificar valor existente

print(persona)

# ➖ Eliminar elementos:
del persona["ciudad"]  # Elimina la clave "ciudad"
print(persona)

# 🔁 Recorrer un diccionario:
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 📋 Métodos útiles:
# .keys()    → devuelve todas las claves
# .values()  → devuelve todos los valores
# .items()   → devuelve pares (clave, valor)

print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))

# 🧠 Diccionario dentro de diccionario:
agenda = {
    "Ana": {"tel": "111", "email": "ana@mail.com"},
    "Luis": {"tel": "222", "email": "luis@mail.com"}
}

print(agenda["Luis"]["email"])  # Acceso a valores anidados

# 📌 ¿Cuándo usar diccionarios?
# - Cuando necesitas asociar claves únicas con valores
# - Para representar estructuras tipo JSON
# - Para almacenar configuraciones o datos relacionados

# 🎓 Ejercicio práctico:
alumno = {
    "nombre": "Laura",
    "notas": [4.5, 3.8, 5.0]
}
promedio = sum(alumno["notas"]) / len(alumno["notas"])
print(f"{alumno['nombre']} tiene un promedio de {promedio:.2f}")
