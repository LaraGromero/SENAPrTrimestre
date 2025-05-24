# #TALLER: Registro simple de producto y calculo de costos 
# Np= input("Ingrese el nombre del producto: ")
# Vp= float(input("Ingrese el valor de este producto: "))
# Cp= int(input("Ingrese la cantidad de producatos: "))
# T1= (Np,Vp)
# L1= [T1,Cp]
# D1= {"producto": L1}
# Re= Vp*Cp
# print (f"El costo total es: ", Re)

# #Taller #2: Factura Multiple.
# print ("---- Taller 2: Factura Multiple. ----")
# P1= input("ingrese el nombre del producto: ")
# V1= float(input("Ingrese el valor de este producto: "))
# C1= int(input("Ingrese la cantidad: "))
# P2= input("ingrese el nombre del producto: ")
# V2= float(input("Ingrese el valor de este producto: "))
# C2= int(input("Ingrese la cantidad: "))
# P3= input("ingrese el nombre del producto: ")
# V3= float(input("Ingrese el valor de este producto: "))
# C3= int(input("Ingrese la cantidad: "))

# T1=(P1,V1)
# T2=(P2,V2)
# T3=(P3,V3)
# L1= [T1,C1]
# L2= [T2,C2]
# L3= [T3,C3]
# D1={"producto":L1,
#     "producto":L2,
#     "Prodcuto":L3}
# RE1=V1*C1
# RE2=V2*C2
# RE3=V3*C3
# TO=RE1+RE2+RE3
# print ("---------------")
# print (f"Producto 1: ",P1,"Valor: ",V1, "Cantidad: ",C1)
# print (f"Producto 1: ",P2,"Valor: ",V2, "Cantidad: ",C2)
# print (f"Producto 1: ",P3,"Valor: ",V3, "Cantidad: ",C3)
# print (f"El valor total de cada prodcuto es: ",RE1,RE2,RE3)
# print ("Valor a pagar:",TO)
 
#Taller #3: REGISTRO DE NOTAS DE UN ESTUDIANTE
print ("---- Taller 3: Registro de Notas de Estudiantes ----")
N= input("Ingrese su nombre: ")
M1= input("Ingrese la primera asignatura: ")
M2= input("Ingrese la 2da asignatura: ")
M3= input("Ingrese la 3ra asignatura: ")
print (f"---- ",M1,"----")
V1= float(input("ingrese una nota: "))
V2= float(input("Ingrese una 2da nota: "))
R1= (V1+V2)/2
print (f"---- ",M2,"----")
V3= float(input("ingrese una nota: "))
V4= float(input("Ingrese una 2da nota: "))
R2= (V3+V4)/2
print (f"---- ",M3,"----")
V5= float(input("ingrese una nota: "))
V6= float(input("Ingrese una 2da nota: "))
R3= (V5+V6)/2
T1= (M1,R1)
L1= [T1,V1,V2]
T2= (M2,R2)
L2= [T2,V3,V4]
T3= (M3,R3)
L3= [T3,V5,V6]
LM= [M1,M2,M3]
DICC= {"Nombre": N,
       "Materias":L1 }
Prom= R1+R2+R3
R=Prom/3

print ("---- BOLETIN ----")
print ("Nombre del estudiante: ", N)
print (M1,"Valor Final: ", R1)
print (M2,"Valor Final: ", R2)
print (M3,"Valor Final: ", R3)

#TERMINADO. UTILIZAR DICC, TUP Y LIS.

