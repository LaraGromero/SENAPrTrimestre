# print ("DIAGRAMA DE FLUJO: SOLICITUD DE CREDITO")

# N=input("Ingrese su nombre: ")
# E=int(input("Ingrese su edad: "))
# if E>=18 :
#     print (f"{N}, puede solicitar su credito")
#     Usuario= input("Ingrese su nombre de usuario: ")
#     Contraseña=float(input("Ingrese la contraseña: "))
#     M=float(input("Ingrese el monto que necesita: "))
#     print (f"{N}, USTED SOLICITO UN CREDITO POR EL MONTO DE: {M}")
# elif E<18:
#     print (f"{N}, no puede solicitar su credito por que no cumple la edad requerida")
# else:
#     print (f"No cumple las instrucciones")
    
# print (f"DIAGRAMA DE FLUJO: ENTRADA A UNA SALA DE JUEGOS")
# print ("""VALORES DE ENTRADA /n BABY (Menores a 4 años) ENTRADA GRATIS/n KIDS (Entre 4 años a 17 años) VALOR ENTRADA 5 EUROS/nADULTS (Mayores a 18 años) VALOR ENTRADA 18 EUROS""") #SIn "f" gracias a /n se puede juntar y con Alt+z se pude organizar en una sola linea y para textos largos triple comilla
# Edad= int(input("Ingrese su edad: "))
# if Edad<4:
#     print (f"Su entrada es GRATIS")
# elif Edad<18 and Edad>4:
#     print ("El valor de entrada para su categoria es 5 EUROS")
# else:
#     print ("El valor de su entrada para su categoria es de 18 EUROS")
    
print ("DIAGRAMA DE FLUJO: Programa que ejecute las cuatro operaciones")
N1=float(input("Ingrese un numero:"))
N2=float(input("Ingrese otro numero: "))
L= input("Escriba el nombre de la operacion que quiere realizar: ").upper()
if L== "SUMA": #Letras en ""
    suma=N1+N2
    print (f"El resultado de la suma es: {suma}")
elif L=="R":
    resta=N1-N2
    print (f"El resultado de su resta es: {resta}")
elif L=="M":
    multi=N1*N2
    print (f"El resultado de la multiplicacion es: {multi}")
elif L=="D":
    divi= N1/N2
    print (f"El restultado de su division es: {divi}")
else:
    print ("No se maneja ese tipo de operacion")