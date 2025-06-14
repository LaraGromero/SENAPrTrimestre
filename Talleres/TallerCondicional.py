# print ("I. Verifica si un número es positivo, negativo o cero")
# N1=float(input("Ingrese un numero: "))
# if N1<0:
#     print (f"{N1}, es un numero negativo")
# elif N1==0:
#     print (f"no es numero positivo ni negativo")
# else: 
#     print (f"{N1}, es numero positivo")
    
# print ("II. Calcula el mayor de dos números ingresados. ")
# N2= int(input("Ingrse un numero: "))
# N3= int(input("Ingrese otro numero: "))
# if N2>N3:
#     print (f"El numero {N2} es mayor que {N3}")
# elif N2==N3:
#     print ("Los dos numeros son iguales")
# else:
#     print (f"El numero {N3} es mayor a {N2}")
    
# print ("III. Determina si un número es par o impar.")
# N3= int(input("Ingrese un numero: "))
# if N3 % 2 == 0:
#     print (f"El numero {N3}  es par")
# else:
#     print (f"El numero {N3} es impar")

# print ("IV. Dado un número, verifica si está entre 10 y 20.")
# N4= int(input("Ingrese un numero: "))
# if N4>10 and N4<20:
#     print ("Esta entre 10 y 20")
# else: 
#     print ("No esta entre 10 y 20")

# print ("V. Dados tres números, encuentra el mayor usando condicionales.")
# N1=int(input("Ingrese un numero: "))
# N2= int(input("Ingrese un numero: "))
# N3= int(input("Ingrese un numero: "))

# if N1>N2 and N1>N3:
#     print (f"El numero mayor es {N1}")
# elif N2>N1 and N2>N3:
#     print (f" El numero mayor es {N2}")
# else:
    
# print ("VI. Calcula el precio final con un 10 % De descuento si el total es mayor a $100")
# N= int(input("Ingrese un precio: "))
# if N>=100:
#     R=N*0.10
#     print (F"El precio final con el descuento incluido es {R}")
# else:
#     print ("Su compra no cumple lo requerido para otener el descuento")
    
# print ("VIi. Verifica si una persona puede votar (mayor o igual a 18 años)")
# Edad= int(input("Ingrese su edad"))
# if Edad>=18:
#     print ("Usted puede votar")
# else: 
#     print ("Usted no puede votar por ser menor de edad")

 
# print ("VIII. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.")
# C= input("Ingrese si usted es cliente normal o VIP: ").upper()
# p= int(input("Ingrese el precio de la compra: "))
# if C=="VIP":
#     Descuento=p*0.20
#     print (f"VIP su precio final es {Descuento}")
# else: 
#     print ("Su precio a pagar sigue siendo el mismo")
    
# print ("IV. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo.")
# N= int(input("Ingrese un numero: "))
# if N % 5 == 0:
#     print ("El numero",N,"Es multiplo de 5")
#     if N %3 == 0:
#         print ("Y tambien es multiplo de 3")
# else:
#     print ("No es multiplo de 5 y 3 a la vez")
        
# print ("X. Dado un número, verifica si es divisible entre dos números dados. ") 
# M= int(input("Ingrese un numero que quiere verificar: "))
# N1= int(input("Ingrese el primer numero en el que se verificara: "))
# N2= int(input("Ingrese el segundo numero en el que se verificara: "))

# if M % N1 == 0 and M % N2 == 0:
#     print (f"El numero es multiplo de {N1} y de {N2}")
# elif M % N1 == 0 and not M %N2 == 0:
#     print (f"El numero es multiplo de {N1} pero no de {N2} ") 
# elif M % N2 == 0 and not M % N3 == 0:
#     print (f"El numero es multiplo de {N2} pero no de {N1} ") 
# else:
#     print ("El numero no es multiplo de ninguno de los dos numeros.")

# print ("Ejercicios con Listas (con condicionales)")

# print ("XI.Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra Mayor a 10, si no, muestra Menor o igual a 10.")
# N1=int(input("ingrese un numero: "))
# N2=int(input("ingrese un numero: "))
# N3=int(input("ingrese un numero: "))
# N4=int(input("ingrese un numero: "))
# N5=int(input("ingrese un numero: "))
# L1= [N1,N2,N3,N4,N5]
# print (L1) 
# if L1[2] > 10:
#     print ("Mayor a 10")
# else:
#     print ("Menor o Igual a 10")

# print ("XII. Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra Está en la lista, si no, muestra “No está en la lista.")
# L2= [3,5,7,9]
# if 7 in list: 
#     print ("Está en la lista")
# else:
#     print ("No está en la lista.")

# print ("XIII. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”. ")
# L1= [4,6,2,8]
# if L1[0]+L1[1] > 10:
#     print ("Suma alta")
# else: 
#     print ("Suma baja")
    
# print ("IX. Dada la lista [Ana, Luis, Pedro, Marta], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.")
# L2=["Ana","Luis","Pedro","Marta"]
# if L1[3] == "Marta":
#     print ("Nombre Correcto")
# else:
#     print ("Nombre diferente")

# print ("XV. Crea una lista con tres colores. Cambia el segundo color solo si es igual a azul, y muestra la lista actualizada.")
# C1= input("Ingrese un color: ")
# C2= input("Ingrese un color: ")
# C3= input("Ingrese un color: ")
# L1= [C1,C2,C3]
# print (L1)
# if L1[1] == "Azul":
#    C4=L1[1]=input("Ingrese otro color: ")
#    L1[1]==C4
#    print (L1)

# print ("Ejercicios con Tuplas (con condicionales)")

# print ("XVI. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”. ")
# T2= (5, 8, 12, 20)
# print (T2)
# if T2[0]<T2[3]:
#     print ("ORDEN ASCENDENTE")
# else: 
#     print ("Orden descendente")

# print ("XVII. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.")
# T1= (25, 32, 28)
# print (T1)
# if T1[1] > 30:
#     print ("edad mayor a 30")
# else:
#     print ("Edad menor o igual a 30")

# print ("XVIII. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.  ")
# Tupla1=(1, 2, 3)
# print (Tupla1)
# ListaN=list(Tupla1)
# if ListaN[1] == 2:
#     ListaN[1] = 10
#     print (ListaN)
# Tupla2=tuple(ListaN)
# print (Tupla2)

# print ("XIX. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.")
# T1= (4, 9)
# if T1[1] > 5:
#     print ("Coordenada alta")
# else: 
#     print ("Coordenada baja")
    
# print ("XX. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.")
# T1= (3, 4)
# T2= (3, 5)
# if T1 == T2:
#     print ("Tuplas iguales")
# else: 
#     print ("Tuplas diferentes")

print ("Ejercicios con Diccionarios (con condicionales) ")

# print ("XXI. Crea un diccionario con {nombre: Juan, edad: 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”. ")
# D= {"Nombre":"Juan",
#     "Edad":17}
# if D["Edad"]>=18:
#     print ("Adulto")
# else:
#     print ("Menor de edad")

# print ("XXII.Crea un diccionario {nombre: Lucía, edad: 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.")
# D= {"Nombre":"Lucia",
#     "Edad":20}
# if D["Edad"]>18:
#     D["Edad"]=21
#     print (f"Esta es el diccionario actualizado {D}")
# else:
#     print ("Dicionario Normal")

# print ("XXIII.Crea un diccionario con {nombre: Carlos}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario. ")
# D= {"Nombre":"Carlos"}
# if "Ciudad" in D:
#     print (f"Ya existe")
# else:
#     D["Ciudad"]="BOGOTÁ"
#     print (f"Diccionario Actualizado {D}")

# print ("XXIV. Dado el diccionario {producto: pan, precio: 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio")
# P= {"Productos":"Pan",
#     "Precio":1200}
# if "Precio" in P:
#     print (P["Precio"])
# else:
#     print ("No hay precio")
    
print ("XXV. Crea un diccionario con {pan: 1200, leche: 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”")

P= {"Pan": 1200,
    "Leche": 2000}
if "Pan" in P:
    print (P["Pan"])
else:
    print ("El producto no esta disponible")

#TERMINADO
