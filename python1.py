#En una planta de producción, se desea realizar una estadística de la producción de cajas por día en
#cada línea de producción. Debe solicitar el ingreso del número de líneas de producción y los días a registrar;
#en la actualidad se tienen hasta 7 líneas de producción, pero pueden encontrarse paradas o en mantenimiento.
#A continuación, se muestra la siguiente tabla ejemplo:
#Líneas Producción	Día 1	Día 2	Día 3	….	Día n	Total
#L2	              120	  240	  125
#L4	              89	  103	  145
#L1	              112	  98	  108
#Total
#Se debe cargar por cada línea de producción (el código debe ser L1 .. L7) la cantidad de cajas producidas (enteros positivos)
# y obtener los totales por línea y por día Luego de completar y totalizar la tabla correspondiente, se debe mostrar la siguiente información:
#-Señalar el día de mayor y menor producción, así como el promedio del total de producción diaria.
#-Señalar la línea de producción con mayor y menor producción, así como el promedio del total de producción por línea.

#creacion y carga de una matriz nxm
n=int(input("Ingrese el numero de filas: "))
m=int(input("Ingrese el numero de columnas: "))
A=[]
for i in range(n):
  A.append([])
for i in range(n):
  for j in range(m):
    if j==0:
      LineaP=input("Ingrese linea de produccion: ")
      A[i].append(LineaP)
    else:
      cantidadCP=int(input("Ingrese cantidad de cajas producidad: "))
      A[i].append(cantidadCP)
for n in A:
  print(n)
#Total por linea
for i in range(len(A)):
  sumaLP=0
  for j in range(1,m):
    sumaLP=sumaLP + A[i][j]       # sumaLP+=A[i][j]
  LP="L"+str(i+1)
  print("En la linea de produccion ",LP," las cajas prodicidas son: ",sumaLP)
#Total por dia
for j in range(1,m):
  sumaDP=0
  for i in range(len(A)):
    sumaDP=sumaDP + A[i][j]       # sumaDP+=A[i][j]
  DP="Dia"+str(j)
  print("En el ",DP," las cajas producidas son: ",sumaDP)
#Dia de mayor produccion
MayorPD=0
for j in range(1,m) :
  for i in range(len(A)):
    if A[i][j]>MayorPD:
      MayorPD=A[i][j]
      DP="Dia"+str(j)
print("En el ",DP," la mayor produccion de cajas es: ",MayorPD)
#Dia de menor produccion
MenorPD=1000000
for j in range(1,m):
  for i in range(len(A)):
    if A[i][j]<MenorPD:
      MenorPD=A[i][j]
      DP="Dia"+str(j)
print("En el ",DP," la menor produccion de cajas es: ",MenorPD)
#Promedio de cajas producidas por dia
for j in range(1,m):
  sumaDP=0
  con=0
  for i in range(len(A)):
    sumaDP+=A[i][j]
    con+=1               # con= con +1
  promPD=sumaDP/con
  DP="Dia"+str(j)
  print("El promedio de cajas producidas en el ",DP," es: ",promPD)


