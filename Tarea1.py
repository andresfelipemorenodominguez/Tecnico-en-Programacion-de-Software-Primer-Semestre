# crea una cadena que contenga la frase "El conocimiento es poder"
# usa el metodo .find() para encontrar la posicion de la palabra "conocimiento" y la palabra "poder" en la cadena.

# mensaje = "El conocimiento es poder"
# print(mensaje.find("conocimiento"))
# print(mensaje.find("poder"))

# mesaje2 = "la practica hace al maestro"
# print(mesaje2.find("practica"))
# print(mesaje2.find("maestro"))

# #pregunta al usuario que ingrese una frase, pregunta tambien un palabra que quiera buscar en la frase y muestre la posicion de la palabra en la frase.

# frase = input("ingrese una frase: ")
# palabra = input("ingrese una palabra a buscar en la frase: ")
# print(frase.find(palabra))

# text = "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"

# print(text.find("Sabia"))
# print(text.find("Caminaba"))
# print(text.find("falanges"))

# #extraer
# print(text[459:655])

# text1 = "La sociedad francesa estaba dividida en estamentos dependiendo de sus clases sociales, el poder mas alto lo tenía el rey, detrás estaban la nobleza y el clero y el nivel mas bajo de poder lo tenia el tercer estado que estaba constituido por la burguesía, los artesanos y los campesinos."

# print(text1.find("burguesía"))
# print(text1.find("bajo"))
# print(text1.find("artesanos"))

# #extraer bajo hasta artesanos
# print(text1[174:269])

#Trabajas en programacion y te piden crear un programa que calcule la nota final de estudiantes del curso de python. la nota final se calcula basandonos en tre notas previas de la cuales, cada una corresponde un porcentaje distinto de la nota final. los porcentajes son los siguientes: 20% de la nota final de la primera nota, 30% de la nota final de la segunda nota, 50% de la nota final de la tercera nota. el programa debe pedir al usuario que ingrese las tres notas y mostrar la nota final calculada.

nombre = input("ingrese su nombre: ")
nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))
por1 = nota1 * 0.2
por2 = nota2 * 0.3
por3 = nota3 * 0.5
nota_final = por1 + por2 + por3
div = nota_final // 3
print("la nota final del estudiante", nombre, " es: ", nota_final)

