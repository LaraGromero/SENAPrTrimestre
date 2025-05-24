x,y,z=1,4,8 #(Asignación Múltiple)
print (x)

print (y)

print (z)



x=y=z=0 #Asignar el mismo valor a varias variables

x=10 
x=x+5
print(x) 

print(y)

print(z)


dato="Laura es su nombre, "
dato+="ella cumplio 15 "
dato+="Y desear adoptar un gato naranja"
print(dato)


a=b=c=0
print(a,b,c)


n=10
n+=5
n*=2
print(n)

texto1="Hola "
texto2="Shakiraaa"
#Concatenación
resultado=texto1+""+texto2
print(resultado)


saludo="hola mundo"
extraccion=saludo[0:5] # []  imprime el indice hasta otro
print(extraccion)


print("----------------------Tarea 1-----------------")
TX="El conocimiento es poder."

TX= TX.find("conocimiento"),TX.find("poder") #.find para encontrar el índice de un elemento
print(TX)


print("----------------------Tarea 2------------------")
tas="La practica hace al maestro."
tas= tas.find("practica"),tas.find("maestro")
print(tas)


print("----------------------Tarea 3------------------")
tsk=input("Ingresa una frase: ")
pre=input("¿Que palabra de tu frase deseas buscar?, Ingresala: ")
posicion=tsk.find(pre)
print("La palabra",pre,"fue encontrada en la posición",posicion)


print("------------Ejercicio 1 --------------")
chuu="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges "

print(chuu)
print("      ")
texto=chuu.find("Sabia")
print("Sabia se encuentra en la posición: ",texto)

inicio=chuu.find("Caminaba")
final=chuu.find("falanges")+len("falanges") #len cuenta la cantidad de indices y en este caso las suma para q la palabra falanges quede completa

seg=chuu[inicio:final]
print(seg)

print("---- EJERCICIO 2 ----")
bua="Quinto, este manjar atraerá una gran clientela a las tabernas, donde los venteros serán seguramente tan prudentes como para procurarse las mejores recetas para prepararlo a la perfección, y consecuentemente ver sus casas frecuentadas por todos los distinguidos caballeros, quienes se precian con justicia de su conocimiento del buen comer: y un diestro cocinero, que sepa cómo agradar a sus huéspedes, se las ingeniará para hacerlo tan caro como a ellos les plazca."

print(bua.find("diestro"))
print(bua.find("plazca"))
print(bua[345:465])


print("---- PORCENTAJE DE NOTAS ----")
N1=int(input("Escribe tu primer nota de valor de 20%: "))
N1=N1*0.2
N2=int(input("Escribe tu segunda nota de valor de 30%: "))
N2=N2*0.3
N3=int(input("Escribe tu tercer nota de valor de 50%: "))
N3=N3*0.5

NF=N1+N2+N3
print("Tu nota final es: ",NF)