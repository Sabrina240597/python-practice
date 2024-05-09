#Calculadora de propinas:
#Crea un programa que solicite al usuario el total de la factura y el 
#porcentaje de propina que desea dejar. El programa debe calcular y mostrar el 
#monto total a pagar, incluyendo la propina.

def calcular_propina(total_factura, porcentaje_propina):
    propina = total_factura * (porcentaje_propina / 100)
    total_a_pagar = total_factura + propina
    return total_a_pagar

def main():
    total_factura = float(input("Ingrese el total de la factura: "))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

    total_a_pagar = calcular_propina(total_factura, porcentaje_propina)
    print("El monto total a pagar, incluyendo la propina, es: $", total_a_pagar)

if __name__ == "__main__":
    main()

###################################################
#Conversor de temperatura:
#Escribe un programa que convierta una temperatura en grados 
#Celsius a grados Fahrenheit. Solicita al usuario la temperatura 
#en Celsius y muestra el resultado de la conversión.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print("La temperatura en grados Fahrenheit es:", fahrenheit)

if __name__ == "__main__":
    main()

###########################################################
#Adivina el número:
#Crea un juego en el que la computadora genere un número aleatorio y 
#el jugador deba adivinarlo. El programa debe dar pistas al jugador, 
#indicando si el número a adivinar es mayor o menor que el número ingresado. 
#El juego debe continuar hasta que el jugador adivine el número correcto.
    
import random

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Ingresa tu suposición: "))
        intentos += 1

        if intento < numero_a_adivinar:
            print("El número que estoy pensando es mayor que", intento)
        elif intento > numero_a_adivinar:
            print("El número que estoy pensando es menor que", intento)
        else:
            print("¡Felicidades! ¡Has adivinado el número en", intentos, "intentos!")
            break

if __name__ == "__main__":
    adivina_el_numero()

##########################################################################
#Contador de vocales:
#Desarrolla un programa que cuente la cantidad de vocales en una cadena de 
#texto ingresada por el usuario. El programa debe mostrar el resultado al final.

def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para contar todas las ocurrencias de vocales
    cadena = cadena.lower()
    # Inicializar un contador para las vocales
    contador_vocales = 0
    # Definir un conjunto de vocales para verificar la existencia de cada una en la cadena
    vocales = {'a', 'e', 'i', 'o', 'u'}
    
    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Incrementar el contador si el caracter es una vocal
        if caracter in vocales:
            contador_vocales += 1
    
    return contador_vocales

def main():
    # Solicitar al usuario que ingrese una cadena de texto
    cadena = input("Ingresa una cadena de texto: ")
    # Contar las vocales en la cadena ingresada
    cantidad_vocales = contar_vocales(cadena)
    # Mostrar el resultado
    print("La cantidad de vocales en la cadena es:", cantidad_vocales)

if __name__ == "__main__":
    main()

#####################################################################
#Calculadora de factorial:
#Escribe una función que calcule el factorial de un número entero ingresado 
#por el usuario. Luego, muestra el resultado

def calcular_factorial(numero):
    # Inicializar el factorial como 1
    factorial = 1
    # Verificar si el número es negativo
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    # Calcular el factorial
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def main():
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Ingresa un número entero para calcular su factorial: "))
    # Calcular el factorial del número ingresado
    resultado = calcular_factorial(numero)
    # Mostrar el resultado
    print("El factorial de", numero, "es:", resultado)

if __name__ == "__main__":
    main()

######################################################################
#Generador de contraseñas:
#Crea un programa que genere contraseñas aleatorias. El programa debe 
#permitir al usuario especificar la longitud de la contraseña y la 
#cantidad de contraseñas a generar.
    
import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
    cantidad = int(input("Ingrese la cantidad de contraseñas a generar: "))

    print("\nContraseñas generadas:")
    for _ in range(cantidad):
        contrasena = generar_contrasena(longitud)
        print(contrasena)

if __name__ == "__main__":
    main()

#####################################################################
#Contador de palabras:
#Escribe un programa que cuente la cantidad de palabras en un 
#texto ingresado por el usuario. No se deben contar los espacios 
#en blanco ni los caracteres de puntuación.
    
def contar_palabras(texto):
    # Definir caracteres de puntuación
    caracteres_puntuacion = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Eliminar caracteres de puntuación del texto
    texto_sin_puntuacion = ''.join(caracter for caracter in texto if caracter not in caracteres_puntuacion)
    # Dividir el texto en palabras utilizando los espacios en blanco como separadores
    palabras = texto_sin_puntuacion.split()
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    return cantidad_palabras

def main():
    texto = input("Ingrese un texto para contar las palabras: ")
    cantidad_palabras = contar_palabras(texto)
    print("La cantidad de palabras en el texto es:", cantidad_palabras)

if __name__ == "__main__":
    main()

###################################################################
#Generador de listas:
#Desarrolla una función que genere una lista de números enteros 
#en un rango dado por el usuario. La función debe permitir 
#especificar el inicio, el fin y el paso entre los números.
    
def generar_lista_enteros(inicio, fin, paso):
    lista_enteros = []
    # Verificar si el paso es positivo o negativo
    if paso > 0:
        # Generar la lista de números enteros en el rango especificado
        for i in range(inicio, fin + 1, paso):
            lista_enteros.append(i)
    elif paso < 0:
        # Generar la lista de números enteros en el rango especificado
        for i in range(inicio, fin - 1, paso):
            lista_enteros.append(i)
    return lista_enteros

def main():
    inicio = int(input("Ingrese el número inicial del rango: "))
    fin = int(input("Ingrese el número final del rango: "))
    paso = int(input("Ingrese el paso entre los números: "))

    lista = generar_lista_enteros(inicio, fin, paso)
    print("La lista de números enteros en el rango dado es:", lista)

if __name__ == "__main__":
    main()

##################################################################
#Verificador de palíndromos:
#Crea un programa que verifique si una palabra ingresada por el 
#usuario es un palíndromo, es decir, si se lee igual de izquierda 
#a derecha y de derecha a izquierda.
    
def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación sin distinguir entre mayúsculas y minúsculas
    palabra = palabra.lower()
    # Comparar la palabra con su reverso
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print("¡", palabra, "es un palíndromo!")
    else:
        print("¡", palabra, "no es un palíndromo!")

if __name__ == "__main__":
    main()

#################################################################
#Simulador de Dado:
#Escribe un programa que simule lanzamientos de un dado. 
#El programa debe permitir al usuario especificar la cantidad de 
#lanzamientos y mostrar los resultados de cada lanzamiento.
    
import random

def lanzar_dado(cantidad):
    print("Resultados de los lanzamientos del dado:")
    for i in range(cantidad):
        resultado = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6 (inclusive)
        print("Lanzamiento", i+1, ":", resultado)

cantidad_lanzamientos = int(input("Ingrese la cantidad de lanzamientos del dado: "))
lanzar_dado(cantidad_lanzamientos)
