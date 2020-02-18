# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:45:17 2020

@author: Yadira Quinchiguango
"""

import numpy as np
import pandas as pd

# 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros
columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,50,60).reshape(10,6)

df1 = pd.DataFrame(registros, columns = columns)

primeros5 = df1.head(5)
ultimos5 = df1.tail(5)

# 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988

columns = ['A','B','C','D']
index = ['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06']
arreglo = np.random.rand(24).reshape(6,4)

df2 = pd.DataFrame(arreglo, columns = columns, index = index)

# 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,50,60).reshape(10,6)

df4 = pd.DataFrame(registros, columns = columns)

df4.columns
df4.values

# 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,50,60).reshape(10,6)

df5 = pd.DataFrame(registros, columns = columns)

df5.describe()

# 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,50,60).reshape(10,6)

df6 = pd.DataFrame(registros, columns = columns)

df6.transpose()

# 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,50,60).reshape(10,6)

df7 = pd.DataFrame(registros, columns = columns)

ascendente = df7.sort_values(columns)
descendente = df7.sort_values('A',ascending=False)

#8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,10,60).reshape(10,6)

df8 = pd.DataFrame(registros, columns = columns)

nuevodf = df8[df8[columns]>7]

#9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,10,60).reshape(10,6)

df9 = pd.DataFrame(registros, columns = columns)

nuevodf = df9[df9[columns]>7].fillna(0)

#10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

columns = ['A','B','C','D','E','F']
registros = np.random.randint(0,10,60).reshape(10,6)

df10 = pd.DataFrame(registros, columns = columns)

media = df10.mean()
mediana = df10.median()
promedio = np.average(df10)

# 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, 
# luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 
# y anadirlo al primer Dataframe

df111 = pd.DataFrame(np.random.randint(0,10,60).reshape(10,6))
df112 = pd.DataFrame(np.random.randint(0,10,60).reshape(10,6))

df111 = df111.append(df112, ignore_index = True)

# 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola,  
# la 3 y 4, y la 5 y 6 concatenando su texto.

A = ["clase 1"] * 5 + ["clase 2"] * 5
B = ["tipo 1"] * 2 + ["tipo 2"] * 3 + ["tipo 3"] * 2 + ["tipo 4"] * 3
C = ["clase 1"] * 5 + ["clase 2"] * 5
D = ["tipo 1"] * 2 + ["tipo 2"] * 3 + ["tipo 3"] * 2 + ["tipo 4"] * 3
E = ["clase 1"] * 5 + ["clase 2"] * 5
F = ["tipo 1"] * 2 + ["tipo 2"] * 3 + ["tipo 3"] * 2 + ["tipo 4"] * 3

df12 = pd.DataFrame({"A": A, "B": B, "C": C, "D": D, "E": E, "F": F })



# 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, 
# obtener la frecuencia de repeticion de los numeros enteros en cada columna

columns = ['A','B','C','D','E','F'] 
registros = np.random.randint(0,10,60).reshape(10,6)

df13 = pd.DataFrame(registros, columns = columns)

columna1 = df13.A.value_counts()
columna2 = df13.B.value_counts()
columna3 = df13.C.value_counts()
columna4 = df13.D.value_counts()
columna5 = df13.E.value_counts()
columna6 = df13.F.value_counts()

# 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. 
# Crear una nueva columna con el calculo por fila (A * B ) / C

columns = ['A','B','C']
registros = np.random.randint(0,10,30).reshape(10,3)

df14 = pd.DataFrame(registros, columns = columns)

df14[4] = df14['A']*df14['B']/df14['C']
df14.columns = ['A','B','C','D']


















