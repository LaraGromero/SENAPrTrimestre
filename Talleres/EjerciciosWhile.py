# print ("---- SUMA HASTA 0 ----")
# total = 0
# num = int(input("Ingrese un numero entero o 0 para terminar: "))

# while num != 0:
#     total += num
#     num=  int(input("Ingrese un numero entero o 0 para terminar: "))
# print (f"La suma total: {total}")

# print ("---- Contraseña Secreta ----")
# clave= "python123"
# dato= input("Ingrese la contraseña: ")
# while clave != dato:
#     print (f"Contraseña incorrecta intentelo de nuevo")
#     dato= input("Ingrese la contraseña: ")
# print ("Contraseña correcta")

# print ("---- Lista de compras  ----")
# L1= []
# while True:
#     Producto= input("Ingrese un producto (o fin para finalizar): ")
#     if Producto.lower() == "Fin":
#         print (f"Progrma Finaliza")
#     else:
#         L1.append(Producto)
#         print (f"La lista de compras es {L1}")

# print ("---- Contador de pares e impares   ----")
# contador= 0
# Pares= 0
# Impares= 0

# while contador < 10:
#     N= int(input(f"Ingrese un numero {contador + 1}: "))
#     if N % 2 == 0:
#         Pares += 1
#     else:
#         Impares += 1
#     contador += 1
# print (f" Total de pares {Pares}")
# print (f"Total de Impares {Impares}")

# print ("---- Promedio de calificaciones ----")
# L1= []
# while True:
#     Nota= float(input("Ingrese una Nota (o 7 para finalizar): "))
#     if Nota == 7:
#         break
#     L1.append(Nota)
# if L1: 
#     Op= sum(L1) / len(L1)  #Sum para la sumatoria de la lista y el len para la cantidad de datos ingresados
#     print (f"El promedio de las notas es:  {Op}")

# print ("---- Tabla de multiplicar interactiva ----")
# contar= "Si"
# while contar.lower() == "si":
#     numero= int(input("Ingresar la tabla de multiplicar: "))
#     contar =1
#     print (f"tabla del {numero}:\n")
    
#     while contar <=10:
#         r= numero * contar
#         print (f"{numero}*{contar}={r}")
#         contar += 1
#         contar= input("Quiere otra tabla(si/no):")

# print ("---- Adivina el número ----")
# NS= 17
# print ("Ingrese un numero para adivinar el Numero secreto")
# while True:
#     Dato= int(input("Ingrese el numero: "))
#     if Dato < NS:
#         print (f"El numero ingresado es menor al numero secreto")
#     elif Dato > NS:
#         print (f"El numero ingresado es mayor al numero secreto")
#     elif Dato == NS:
#         print ("Has adivinado!")
#         break

# print ("---- Tupla de frutas ----")
# Frutas= ["Banano","Guanabana","Naranja"]
# print ("Intente adivinar una de las frutas misteriosas")
# while True:
#     Dato= input("Ingrese una fruta: ")
#     if Dato.capitalize() in Frutas: #.capitalize para la primera letra en mayus
#         print ("Has adivinado.")
#         break
    
# print ("---- Diccionario de traducción ----")
# palabras= {
#     "cama": "bed",
#     "ventana": "window",
#     "puerta": "door",
#     "perro": "dog",
#     "gato": "cat"
# }
# while True:
#     Dato= input("Ingrese una palabra (o fin para terminar el programa): ").lower()
#     if Dato == "fin":
#         print ("Terminaste el programa")
#         break
#     elif Dato in palabras:
#         V= palabras[Dato]
#         print (f"La traduccion de {Dato} es {V}")
    
    
# print ("---- Calculadora básica ----")
# while True:
#     print ("""Ingrese una de las siguientes opciones:/n
#            Op 1 Suma
#            Op 2 Resta
#            Op 3 Multiplicación
#            Op 4 Division
#            Op 5 Salir""")
#     V= int(input("ingrese el Numero de una de las opciones: "))
#     if V == 1:
#         N1= int(input("Ingrese un numero: "))
#         N2= int(input("Ingrese otro numero: "))
#         Op= N1+N2
#         print (f"La suma de {N1} y {N2} es {Op}")
#     elif V == 2:
#         N1= int(input("Ingrese un numero: "))
#         N2= int(input("Ingrese otro numero: "))
#         Op= N1-N2
#         print (f"La resta de {N1} y {N2} es {Op}")
#     elif V == 3:
#         N1= int(input("Ingrese un numero: "))
#         N2= int(input("Ingrese otro numero: "))
#         Op= N1*N2
#         print (f"La multiplicacion de {N1} y {N2} es {Op}")
#     elif V == 4:
#         N1= int(input("Ingrese un numero: "))
#         N2= int(input("Ingrese otro numero: "))
#         Op= N1/N2
#         print (f"La division de {N1} y {N2} es {Op}")
#     elif V == 5:
#         print("Usted salio del programa")
#         break

# print ("---- Registro de edades ----")
# D1= {}
# while True:
#     Nombre= input("Ingrese un nombre (o fin para finalizar): ").lower()
#     if Nombre == "fin":
#         print (f"Progrma Finaliza")
#         break
#     Edad= int(input("Ingrese la edad (o fin para finalizar): "))
#     D1[Nombre]=Edad
# print (f"La lista de compras es {D1}")

# print ("----  Buscar en lista ----")
# L1= ["Azul","Naranja","Rojo","Verde","Morado"]
# print ("Intente adivinar una de los colores")
# while True:
#      Dato= input("Ingrese un color: ")
#      if Dato.capitalize() in L1: 
#          print ("Has adivinado.")
#          break

# print ("---- Potencias de un número ----")
# N1= int(input("Ingresa un numero: "))
# contador = 1
# print (f"Potecnias del {N1} hasta el 5\n")

# while contador <=5:
#     result= N1 ** contador
#     print (f"{N1}**{contador}={result}")
#     contador += 1

# print ("---- Lista de cuadrados ----")
# C1= 0
# C2= 0
# C3= 0
# C4= 0
# C5= 0
# contador= 1
# while contador <= 5:
#     N= int(input("Ingresa un número: "))
#     if contador == 1:
#         C1= N*N
#     elif contador == 2:
#         C22= N*N
#     elif contador == 3:
#         C3= N*N
#     elif contador == 4:
#         C4= N*N
#     elif contador == 5:
#         C5= N*N
#     contador += 1
# print(f"Estos son los cuadrados ingresados: {C1},{C2},{C3},{C4},{C5}")

E= {}
while True:
    N= input("Ingresa el nombre del estudiante (o 'fin' para salir): ").lower()
    if N == "fin":
        print (f"Progrma Finaliza")
        break
    Calificacion= input(F"Ingresa la nota final de {N}:")
    E[N] =Calificacion
print(f"Diccionario de estudiantes con sus notas:{E}")