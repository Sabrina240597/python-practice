#Escribe un programa que imprima en la consola.
print("bazinga")



#Solicitar al usuario dos números enteros
numero1 = input("ingrese el primer numero...")

numero2 = input("ingrese el segundo numero...")



# Calcular a suma de los dos números
suma = int(numero1) + int(numero2)

# Imprimir la suma
print("la suma de", numero1 ,"y", numero2 , "es", suma )



#crear una calculadora
numero1 = input("ingrese su primer numero...")

operacion= input("ingrese la operacion deseada...")

numero2 = input("ingrese su segundo numero...")

#Realizar la operación correspondiente
if operacion == '+':
    resultado = int(numero1) + int(numero2)
elif operacion == '-':
    resultado =int(numero1) - int(numero2)
elif operacion == '*':
    resultado = int(numero1) *int(numero2)
elif operacion == '/':
    resultado =int(numero1) / int(numero2)
else:
    resultado = "Operación inválida"

print("su resultado es...", resultado)



#Inicializar una variable para contar los números pares
contador = 0

#Inicializar una variable para almacenar el número actual
numero = 0

#hasta que se encuentren los primeros 10 números pares
while contador < 10:
    #Verificar si el número actual es par
    if numero % 2 == 0:
        #Imprimir el número par
        print(numero)
        #Incrementar el contador de números pares
        contador += 1
    #Incrementar el número actual
    numero += 1



#contador de palabras
oracion = input("ingrese una oracion: ")

palabras = oracion.split()
cantidad_palabras = len(palabras)

print("la oracion ingresada tiene", cantidad_palabras, "palabra(s)")

#conversor de temperatura
temperatura_celsius = float(input("ingrese la temperatura en grados celsius: "))

#formula segun el chatGPT para convertir: (0°C × 9/5) + 32 = 32°F
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print("la temperatura en grados fahrenheit es:", temperatura_fahrenheit)



#adivina el numero
import random

numero_adivinar = random.randint(1,100)

while True:
    numero_ingresado = int(input("ingrese un numero: "))

    if numero_ingresado == numero_adivinar :
        print("adivinasteee!")
        break
    elif numero_ingresado < numero_adivinar  :
        print("es chico")

    else:
        print("es grande")




#generador de contrasenias
import random
import string

longitud = int(input("Ingrese que tan grande quiere que sea su contrasenia: "))

caracteres_validos = string.ascii_letters + string.digits + string.punctuation

contrasenia = ''.join(random.choice(caracteres_validos) for _ in range(longitud))

print("Contrasenia generada:", contrasenia)



#calcular un triangulo
base = float(input("Ingresar la base del triángulo: "))

altura = float(input("Ingresar la altura del triángulo: "))

area = (base * altura) / 2

print("El área del triángulo es:", area)




# Crear una lista
lista = []

while True:
    elemento = input("Ingresa un elemento (o 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break
    lista.append(elemento)

print("Lista completa:", lista)



#calculadora de promedio de notas:
#lista para almacenar las notas
notas = []

# Solicitar al usuario ingresar las notas
while True:
    nota = input("Ingrese una nota (o ingrese -1 para finalizar): ")
    if nota == "-1":
        break
    notas.append(float(nota))

# Verificar si se ingresaron notas
if len(notas) > 0:
    # Calcular el promedio de las notas
    promedio = sum(notas) / len(notas)
    # Mostrar el promedio de las notas por pantalla
    print("El promedio de las notas ingresadas es:", promedio)
else:
    print("No se ingresaron notas.")

import collections



# Solicitar al usuario ingresar el nombre del archivo de texto
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Leer el archivo de texto
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()

# Procesar el contenido del archivo
palabras = contenido.lower().split()
frecuencia_palabras = collections.Counter(palabras)

# Identificar las palabras más frecuentes
palabras_mas_frecuentes = frecuencia_palabras.most_common()

# Mostrar las palabras más frecuentes y su conteo en orden descendente
print("Palabras más frecuentes:")
for palabra, conteo in palabras_mas_frecuentes:
    print(palabra, ":", conteo)




#comprobador de palindromos
import string

# Solicitar al usuario ingresar una palabra o frase
palabra = input("Ingresa una palabra o frase: ")

# Eliminar espacios y signos de puntuación
palabra = palabra.replace(" ", "")
palabra = palabra.translate(str.maketrans("", "", string.punctuation))

# Convertir a minúsculas
palabra = palabra.lower()

# Comprobar si es un palíndromo
if palabra == palabra[::-1]:
    print("La palabra o frase es un palíndromo.")
else:
    print("La palabra o frase no es un palíndromo.")




#Validador de Números de Tarjeta de Crédito
# Solicitar al usuario ingresar un número de tarjeta de crédito
numero_tarjeta = input("Ingresa un número de tarjeta de crédito: ")

# Verificar si el número de tarjeta tiene el formato correcto y contiene 
# solo dígitos numéricos
if not numero_tarjeta.isdigit() or len(numero_tarjeta) != 16:
    print("El número de tarjeta de crédito es inválido.")
    exit()

# Implementar el algoritmo de Luhn para verificar la validez del 
# número de tarjeta de crédito
digits = [int(d) for d in numero_tarjeta]
digits = digits[::-1]  # Invertir los dígitos para facilitar el procesamiento

for i in range(1, len(digits), 2):
    digits[i] *= 2
    if digits[i] >= 10:
        digits[i] = digits[i] // 10 + digits[i] % 10

total = sum(digits)

if total % 10 == 0:
    print("El número de tarjeta de crédito es válido.")
else:
    print("El número de tarjeta de crédito es inválido.")




#generador de horarios:
from datetime import datetime, timedelta

# Definir la lista de asignaturas con nombres y horarios
from datetime import datetime, timedelta

# Definir una lista de asignaturas con nombres y horarios
asignaturas = [
    {"nombre": "Matemáticas", "horario": {"inicio": datetime(2023, 5, 18, 8, 0), "fin": datetime(2023, 5, 18, 9, 30)}},
    {"nombre": "Física", "horario": {"inicio": datetime(2023, 5, 18, 10, 0), "fin": datetime(2023, 5, 18, 11, 30)}},
    {"nombre": "Historia", "horario": {"inicio": datetime(2023, 5, 18, 12, 0), "fin": datetime(2023, 5, 18, 13, 30)}},
    # Añade más asignaturas aquí con sus respectivos horarios
]

def horarios_se_superponen(horario1, horario2):
    return horario1["inicio"] < horario2["fin"] and horario1["fin"] > horario2["inicio"]

def generar_horario(asignaturas):
    horario = []
    for i in range(len(asignaturas)):
        asignatura_actual = asignaturas[i]
        superpuesto = False
        for j in range(i):
            if horarios_se_superponen(asignatura_actual["horario"], horario[j]["horario"]):
                superpuesto = True
                break
        if not superpuesto:
            horario.append(asignatura_actual)
    return horario

horario_generado = generar_horario(asignaturas)

# Mostrar el horario generado al usuario
for asignatura in horario_generado:
    inicio = asignatura["horario"]["inicio"].strftime("%H:%M")
    fin = asignatura["horario"]["fin"].strftime("%H:%M")
    print(f"{asignatura['nombre']}: {inicio} - {fin}")




#Buscador de Archivos
import os
# Función para buscar archivos en el directorio raíz y sus subdirectorios
def buscar_archivos(directorio, patron):
    archivos_encontrados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if patron in archivo:
                ruta_completa = os.path.join(raiz, archivo)
                archivos_encontrados.append(ruta_completa)
    return archivos_encontrados

# Solicitar al usuario ingresar el directorio raíz y el patrón de búsqueda
directorio_raiz = input("Ingresa el directorio raíz: ")
patron_busqueda = input("Ingresa el patrón de búsqueda: ")

# Realizar la búsqueda de archivos y mostrar los resultados
resultados = buscar_archivos(directorio_raiz, patron_busqueda)

if len(resultados) > 0:
    print("Archivos encontrados:")
    for archivo in resultados:
        print(archivo)
else:
    print("No se encontraron archivos que coincidan con el patrón de búsqueda.")


#Pythagorean
import math

#ingresar los números
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

#Calcular la hipotenusa utilizando la ecuación de Pitágoras
Hipotenusa = math.sqrt(a**2 + b**2)

#printear el resultado
print("La hipotenusa es:", Hipotenusa)

#resultado elevado a la 2
resultado = Hipotenusa**2

#printear el resultado
print("el resultado es:", resultado)

#funcion cuadratica
import math

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

def funcion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        return "La ecuación no tiene soluciones reales."
soluciones = funcion_cuadratica(a, b, c)
print(soluciones)

#La declaración return finaliza la ejecución de la función y devuelve el valor o 
#valores especificados. Esto permite que podamos almacenar el resultado de la 
#función en una variable y utilizarlo posteriormente en nuestro programa. 
#En el ejemplo que te proporcioné, almacenamos las soluciones de la función 
#en la variable soluciones y luego las imprimimos en la última línea del código

#el discriminante es un valor que se utiliza para determinar la naturaleza 
#de las soluciones de la ecuación. El discriminante se calcula como el 
#resultado de la expresión b^2 - 4*a*c. Dependiendo del valor del discriminante
