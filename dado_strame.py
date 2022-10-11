import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# s=0
# n= int(input("Inserte el numero de dados deseados: "))
# matriz_dados=np.zeros([n,7])
# sumas=np.array([0,1,2,3,4,5,6])
# m=0
# list=[]
# for i in range (n):
#     for j in range (7):
#         matriz_dados[i,j]=m
#         m+=1
#     m=0




n= int(input("Inserte el numero de dados deseados: "))
cont=0
matriz_CEROS=np.zeros([6**n,n])


lista=[]

for i in range(0,n):
  lista.append(6**i)

o=1
f=1
c=0
z=1
h=1
w=1

for q in range (6**n):
    matriz_CEROS[q,0]=z
    z+=1
    if z==7:
      z=1

lista= np.array(lista)
print(lista)

yes=1
inicio = 36
final=inicio
estresado=7
for i in lista:
  if i!=1:
    resureccion=inicio 
    for q in range (6**n):
      matriz_CEROS[q,o]=h
      if(q+1==i*f):
        h+=1
        f+=1



      if(q==inicio-1):
          h=1
          if(o<3):
            inicio=inicio+final
          else:
            inicio=inicio+resureccion
          if(q==(6**n)-1):
            if o!=n:
              o=o+1
              f=1
              inicio=final*(6**yes)
              yes=yes+1



matriz_CEROS=pd.DataFrame(matriz_CEROS)
    

print(matriz_CEROS)

matriz_1=np.zeros([6**n,1])
o=1
a=36
p=216
for i in range(6**n):
  matriz_1[i]=o
  if (i==a-1):
    o+=1
    a+=36

  if(i==p-1):
    o=1
    p+=216
matriz_1=pd.DataFrame(matriz_1)





if(n>2):
  matriz_CEROS=matriz_CEROS.drop([2],axis=1)
  matriz_CEROS = pd.concat([matriz_CEROS, matriz_1], axis=1)

  print(matriz_CEROS)


contador=0
matriz_resultados=np.zeros([6**n,1])
matriz_CEROS=np.array(matriz_CEROS)

for i in range (6**n):
  for j in range (n):
    contador=contador+matriz_CEROS[i,j]

  matriz_resultados[i] =contador
  contador=0

print(matriz_resultados)

p=int(input("Ingrese el numero que desea la probabilidad: "))
contador=0
for i in matriz_resultados:
  if i==p:
    contador+=1

print(contador)

contador=n
x=np.zeros((6*n)-(n-1))
for i in range(x.size):
  x[i]=contador
  contador+=1

print(x)

contador=n
y=np.zeros(6*n)
cont_1=0


for p in range(6*n):
  for i in matriz_resultados:
    if(i==contador):
      cont_1+=1
  y[p]=cont_1
  contador+=1
  cont_1=0
y=y[y!=0]
print(y)


plt.scatter(x,y)
plt.show()