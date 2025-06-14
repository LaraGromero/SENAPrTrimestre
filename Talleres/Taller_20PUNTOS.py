print ("-----TALLER DE TUPLAS-----")
# print ("-----EJERCICIO 1-----")
# N1= (88,42,36,41,65)
# v= (N1[0])
# v2= (N1[-1])
# print (v)
# print (v2)

# print ("-----EJERCICIO 2-----")
# N1= [8.8,4.2,3.6,4.1,6.5]
# v= (N1[1])
# v2= (N1[-2])
# print (v)
# print (v2)

# print ("-----EJERCICIO 3-----")
# N1= ("Balon", "Naranja", "Sombrero")
# Dep=(N1[0])
# Com= (N1[1])
# Rop= (N1[2])

# print ("El siguiente elemento corresponde a los deportes: ",Dep)
# print ("El siguiente elemento corresponde a las comidas: ",Com)
# print ("El siguiente elemento corresponde a los ropa: ",Rop)

# print ("-----EJERCICIO 4-----")
# L1= [17,4,38,8,100]
# Res= L1[0]+L1[1]+L1[2]+L1[3]+L1[4]
# print (Res)

# print ("-----EJERCICIO 5-----")
# T1= (3.4,1.2,7.8)
# Res= T1[0]+T1[1]+T1[2]
# R= Res/3
#  print (R)

# print ("-----EJERCICIO 6-----")
# L1= [5, 3, 6, 1]
# G1= (L1[0])
# G2= (L1[1])
# G3= (L1[2])
# G4= (L1[3])

# print ("Asignada a: ",G1)
# print ("Asignada a: ",G2)
# print ("Asignada a: ",G3)
# print ("Asignada a: ",G4)

# print ("-----EJERCICIO 7-----")
# T1= (3,88)
# R= T1[0]*T1[1]
# print (R)

# print ("-----EJERCICIO 8-------")
# L1= ["Hola","COMO", 7]
# L1.append (67)
# P1= (L1[0])
# P2= (L1[-1])
# print (L1)
# print (P1)
# print (P2)

# print ("-----EJERCICIO 9-----")
# t1= (45,76,23,12)
# A= (t1[0])
# B= (t1[1])
# r= A+B
# print (r)

# print ("-----EJERCICIO 10-----")

# L1= [1,3,5,7,9]
# r= L1[4]-L1[0]
# print (r)

print ("-----EJERCICIO 11-----")
T1=(5,6,7,8,9,10)
print(T1)
M1=T1[0]*T1[-1]
print("El resultado de la multiplicación del primer y último elemento es: ",M1)


print("----EJERCICIO 12----")
T12=[50,25,100]
print(T12)
D12=T12[0]/T12[-1]
print("El resultado de la división entre el primer y el tercer número es de: ", D12)


print("----EJERCICIO 13----")
T13=(2,4,6,8)
print(T13)
print("El tercer elemento de la tupla es: ",T13[2])


print("---- EJERCICIO 14 ----")
T14= [0.1,0.4,6.3,2.5,1.6]
print(T14)
S14=T14[0]+T14[1]+T14[2]+T14[3]+T14[4]
print ("La suma de todos los elementos de la lista es de: ",S14)


print("---- EJERCICIO 15 ----")
T15=[56,34,31,48]
print(T15)
LT15p=tuple(T15) 
print ("La lista: ",T15," convertida en una tupla: ",LT15p)


print ("----EJERCICIO 16----")
T16=(5,40,80,)
print("La tupla es: ",  T16)
LT16=list(T16) 
print("Ahora la tupla convertida en una lista es ",LT16)
LT16.append(int(input("Agrega un numero a la lista: "))) 
print("Ahora tu lista es: ",LT16)


print("---- Ejercicio 17 ----")
T17=["Banano","Papaya","Mango","Manzana","Fresa"]
print("La lista es: ",T17)
LT17=tuple(T17)
print("Ahora la lista convertida en una tupla es : ",LT17," y su tercer elemnto es: ",LT17[2])


print("----EJERCICIO 18----")
T18=(48,95,12)
LT18=list(T18)
print("La tupla es: ",T18,"Ahora convertida en lista es: ",LT18)
nm=(int(input("¿Qué número del medio es el correcto según la secuencia? :")))
LT18[1]=nm  
print("Ahora tu lista es: ",LT18)


print("----EJERCICIO 19----")
T19=[30,65,9,122]
LT19=tuple(T19)
print("Ahora la lista ",T19," convertida a tupla es: ",LT19," y la cantidad de elementos de la tupla es: ",len(LT19))


print("------------------EJERCICIO 20----------------")
T20=(15,28,33,45,57)
LT20=list(T20)
print("La tupla ",T20," convertida en lista es ", LT20)
LT20.pop() #.pop elimina o devuelve un elemento según un índice (el último si no se le coloca nada)
print("Ahora tu lista removiendo el último elemento es: ",LT20)

#practica de todos los metodos.