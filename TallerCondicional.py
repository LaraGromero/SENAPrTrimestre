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
    
print ("VI. Calcula el precio final con un 10 % De descuento si el total es mayor a $100")
N= int(input("Ingrese un precio: "))
if N>=100:
    R=N*0.10
    print (F"El precio final con el descuento incluido es {R}")
else:
    print ("Su compra no cumple lo requerido para otener el descuento")
    
print ("VIi. Verifica si una persona puede votar (mayor o igual a 18 años)")
Edad= int(input("Ingrese su edad"))
if Edad>=18:
    print ("Usted puede votar")
else: 
    pritn ("Usted no puede votar por ser menor de edad")

 
print ("VIII. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.")
C= input("Ingrese si usted es cliente normal o VIP: ").upper()
p= int(input("Ingrese el precio de la compra: "))
if C=="VIP":
    Descuento=p*0.20
    print (f"VIP su precio final es {Descuento}")
else: 
    print ("Su precio a pagar sigue siendo el mismo")