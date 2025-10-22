#Crea un archivo de Python llamado bucle_for_basico1.py y realiza lo presentado a continuación:

#1.- Básico: imprime todos los números enteros del 0 al 100.
for num in range(0,101):
    print(num,end = ' ')
print("\n")

#2.- Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

for numero in range(2,501,2):
    print(numero,end = ' ')
print("\n")

#3.-Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número.
#   Si es divisible por 10, imprime “baby”

for i in range(1,101):
    if i % 5 == 0:
        print("ice ice",end = ' ')
    if i % 10 == 0:
        print("baby",end = ' ')
print("\n")

#4.-Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).

suma=0
for n in range(0,500001,2):
    if n % 2 == 0:
        suma = suma+ n
print("la suma de los numeros pares es:",suma)
print("\n")

#5.-Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

for n in range(2024,0,-3):
    print(n,end = ' ')
print("\n")

#6.-Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, 
# imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, 
# el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

numInicial = int(input("ingresa numero inicial: "))
numFinal = int(input("ingresa numero final: "))  
multiplo = int(input("ingresa el numero de múltiplo:"))

for i in range(numInicial,numFinal +1):
    if i % multiplo == 0: 
        print(i)
