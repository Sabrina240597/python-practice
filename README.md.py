#como se hace una suma o otro tipo de calculo:

#Solicitar al usuario dos números enteros
numero1 = input("ingrese el primer numero...")

numero2 = input("ingrese el segundo numero...")

#Calcular a suma (o otro tipo de calculo) de los dos números
suma = int(numero1) + int(numero2)

#Imprimir la suma
print("la suma de", numero1 ,"y", numero2 , "es", suma )

######################################################################

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
#####################################################################