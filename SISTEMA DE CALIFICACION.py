print ("--- Sistema de Calificación ---")
nb=input("ingrese su nombre: ")
nm=float(input("ingrese la nota minima para aprobar: "))

print ("--- PRIMERA MATERIA ---")

Mp= input("ingrese el nombre de la materia que quiere promediar: ")
p1= float(input("ingrese la primera nota: "))
p2= float(input("Ingrese la segunda nota: "))
p3=float(input("ingrese la tercera nota: "))

Rep= p1+p2+p3
Pr= Rep/3
Cp= nm<=Pr

print (nb,"su nota final en la asignatura de: ",Mp, "Es de: ", Pr)
print ("¿Ud aprueba la materia? ",Cp)

print ("--- SEGUNDA MATERIA ---")

Mt= input("ingrese el nombre de la materia que quiere promediar: ")
T1= float(input("ingrese la primera nota: "))
T2= float(input("Ingrese la segunda nota: "))
T3=float(input("ingrese la tercera nota: "))

ReT= T1+T2+T3
Tr= ReT/3
Ct= nm<=Tr

print (nb,"su nota final en la asignatura de: ",Mt, "Es de: ", Tr)
print ("¿Ud aprueba la materia? ",Ct)

print ("--- TERCERA MATERIA ---")

Ms= input("ingrese el nombre de la materia que quiere promediar: ")
s1= float(input("ingrese la primera nota: "))
s2= float(input("Ingrese la segunda nota: "))
s3=float(input("ingrese la tercera nota: "))

Res= s1+s2+s3
Sr= Res/3
Cs= nm<=Sr

print (nb,"su nota final en la asignatura de: ",Ms, "Es de: ", Sr)
print ("¿Ud aprueba la materia? ",Cs)

print ("--- CUARTA MATERIA ---")

Ml= input("ingrese el nombre de la materia que quiere promediar: ")
L1= float(input("ingrese la primera nota: "))
L2= float(input("Ingrese la segunda nota: "))
L3=float(input("ingrese la tercera nota: "))

Rel= s1+s2+s3
Lr= Rel/3
Cl= nm<=Lr

print (nb,"su nota final en la asignatura de: ",Ml, "Es de: ", Lr)
print ("¿Ud aprueba la materia? ",Cl)

print ("--- QUINTA MATERIA ---")

Mw= input("ingrese el nombre de la materia que quiere promediar: ")
W1= float(input("ingrese la primera nota: "))
W2= float(input("Ingrese la segunda nota: "))
W3=float(input("ingrese la tercera nota: "))

Rew= W1+W2+W3
Wr= Rew/3
CW= nm<=Wr

print (nb,"su nota final en la asignatura de: ",Mw, "Es de: ", Wr)
print ("¿Ud aprueba la materia? ",CW)

print ("--- PROMEDIO GENERAL ---")
G= Pr+Tr+Sr+Lr+Wr
Gr= G/5
print (f"El promedio de las 5 asignaturas es de: ", Gr)

#TERMINADO, CALIFICACION, PROGRAMA.