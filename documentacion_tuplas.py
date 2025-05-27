# Documentación sobre Tuplas en Python

# ¿Qué es una Tupla?
# Una tupla es una estructura de datos en Python que permite almacenar una colección
# ordenada e inmutable de elementos.

mi_tupla = (1, 2, "hola", 3.14)

# Características de las Tuplas
# - Inmutables
# - Ordenadas
# - Indexables
# - Iterables
# - Permiten duplicados
# - Más eficientes que las listas para datos inmutables

# Sintaxis
tupla = (1, 2, 3)
tupla_sin_parentesis = 1, 2, 3
tupla_uno = (5,)  # Tupla de un solo elemento
no_tupla = (5)    # Esto es un entero

# Acceso a Elementos
mi_tupla = (10, 20, 30, 40)
print(mi_tupla[0])      # 10
print(mi_tupla[-1])     # 40

# Desempaquetado
a, b, c = (1, 2, 3)
print(a, b, c)

# Métodos de las Tuplas
t = (1, 2, 3, 2, 2)
print(t.count(2))  # 3
print(t.index(3))  # 2

# Operaciones con Tuplas
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4)

t4 = t1 * 2
print(t4)  # (1, 2, 1, 2)

# Uso de Tuplas en Funciones

# Como argumentos
def ejemplo(a, b, c):
    print(a, b, c)

valores = (1, 2, 3)
ejemplo(*valores)

# Como retorno de múltiples valores
def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(x, y)

# Comparación con Listas
# Tupla: Inmutable, (), más rápida
# Lista: Mutable, [], más métodos

# Casos de Uso Comunes
personas = [("Juan", 25), ("Ana", 30), ("Luis", 22)]
for nombre, edad in personas:
    print(f"{nombre} tiene {edad} años")

ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles"
}

# Buenas Prácticas
# - Usa tuplas si los datos no deben cambiar
# - Son ideales para retornar múltiples valores
# - Muy útiles para claves de diccionarios

# Conclusión:
# Las tuplas son estructuras de datos eficientes, inmutables y ordenadas que deben usarse
# cuando no se necesita modificar la colección de elementos.
