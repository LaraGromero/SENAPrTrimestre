print ("---- EJERCICIOS ----")

print ("---- PRODCUTOS DE UNA BOLSA ----")
pb= [""]
pb.append (input("ingrese 3 productos que desees comprar a la lista"))
print (pb)

print ("--- PRECIO DE 3 ARTICULOS ---")
p1=float(input("ingrese el primer precio: "))
p2=float(input("Ingrese el segundo precio: "))
p3=float(input("ingrese el tercer precio: "))
precios= [p1,p2,p3]
suma= precios[0]+precios[1]+precios[2]
print (f"La sumatoria de su compra fue: ",suma)

print ("---- NUMEROS POR EL USUARIO ----")
numeros= []
numeros.append(int(input("ingrese un numero: ")))
numeros.append(int(input("ingrese otro numero: ")))
numeros.append(int(input("ingrese uj ultimo numero: ")))
print (f"El numero mayor es: {max(numeros)} y el menor fue: {min(numeros)}")

#EJERCICIOS GUIA SOCIALIZACIÓN.