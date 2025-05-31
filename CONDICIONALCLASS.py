# E=int(input("Ingrese su edad:")) 
# if E < 18: 
#     print ("Usted es menor de edad")
# else: 
#     print ("Usted es mayor de edad")
    
    
# #Multiples If en un identacion.
# X=25
# if X>10:
#     print ("Por encima de diez")
#     if X>20:   #Se puede colocar otro if dentro de la identacion del primero pero jamas dos if seguidos sin que ni uno de ellos este dentro del otro. 
#         print ("y tambien pro encima de 20")
#     else:
#         print("pero no por encima de 20")
        

# print ("---- EJERCICIO ----")
# A= int(input("Ingrese un numero: "))
# B= int(input("Ingrese otro numero: "))
# C= A*B
# if C<50:
#     print (C,"Es menor que 50")
# elif C<=10:
#     print (C,"Es menor o igual a 100")
# elif C>100:
#     print (C,"Es mayor a 100")
# else: 
#     print ("No cumple")
    
print ("---- EJERCICIO ----")
Año= int(input("Ingrese su año de nacimiento: "))
if Año<=1940:
    print ("Generacion Silenciosa")
elif Año<=1964:
    print ("Baby bommer")
elif Año<=1979:
    print ("Generacion X")
elif Año<=2000:
    print ("Generacion Y")
else: 
    print ("Generacion Z")