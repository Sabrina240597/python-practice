#como se hace una suma o otro tipo de calculo:

#Solicitar al usuario dos números enteros
numero1 = input("ingrese el primer numero...")

numero2 = input("ingrese el segundo numero...")

#Calcular a suma (o otro tipo de calculo) de los dos números
suma = int(numero1) + int(numero2)

#Imprimir la suma
print("la suma de", numero1 ,"y", numero2 , "es", suma )

######################################################################################

#creando una calculadora

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
#######################################################################################

#contador de numeros pares:

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

#######################################################################################

#contador de palabras

oracion = input("ingrese una oracion: ")

palabras = oracion.split()
cantidad_palabras = len(palabras)

print("la oracion ingresada tiene", cantidad_palabras, "palabra(s)")

########################################################################################

#conversor de temperatura

######conversor de °C a °F:######
temperatura_celsius = float(input("ingrese la temperatura en grados celsius: "))

#formula segun el chatGPT para convertir: (0°C × 9/5) + 32 = 32°F
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print("la temperatura en grados fahrenheit es:", temperatura_fahrenheit)

######conversor de °F a °C:######
temperatura_fahrenheit = float(input("ingresar la temperatura en grados fahrenheit: "))

#formula: (0*F - 32) / 1,8
temperatura_celsius = (temperatura_fahrenheit - 32) / 1.8
print("la temperatura en grados celsius es:", temperatura_celsius)

########################################################################################

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

###########################################################################################

