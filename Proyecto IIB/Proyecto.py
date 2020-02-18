# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 09:45:55 2019

@author: Yadira Quinchiguango
"""

import pandas as pd
import matplotlib.pyplot as plt

path = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto IIB//brickset-scraper//brickset.csv"
df= pd.read_csv(path, encoding = 'unicode_escape',sep = ",")

# Mayor Dificultad  
plt.figure(figsize=(6,3))
plt.title('Mayor Dificultad')
plt.xlabel("Número de piezas")
plt.ylabel("Producto")
mayor_numero_piezas = df.sort_values('pieces',ascending=False)[:5]
x=mayor_numero_piezas["pieces"]
y=mayor_numero_piezas["name"]
plt.scatter(x,y, s = (20*1)**2, color = ["red","green","blue","yellow", "brown"], alpha=0.5)
plt.show()

plt.figure(figsize=(6,3))
plt.title('Puntuación de productos')
mayor_rating = df.sort_values('rating',ascending=False)[:300]
mayor_rating.rating.value_counts().plot(kind='barh', color = "Green", alpha=0.5)
plt.show()

plt.figure(figsize=(6,3))
plt.title("Minifiguras")
minifiguras = df.sort_values('minifigs',ascending=False)[:10]
y = minifiguras["name"]
x = minifiguras["minifigs"]
plt.plot(x,y)
plt.show()


rating = df['rating'].dropna()
rango_rating = [int(r) for r in rating]
entre0y2 = 0  
entre2y3 = 0
entre3y4 = 0
entre4y5 = 0

for i in rango_rating:
    if(i <= 2):
        entre0y2 = entre0y2 + 1
    elif(i <= 3 and i > 2):
        entre2y3 = entre2y3 + 1
    elif(i <= 4 and i > 3):
        entre3y4 = entre3y4 + 1
    else:
        entre4y5 = entre4y5 + 1

rangos = [entre0y2, entre2y3, entre3y4, entre4y5]
rangos_etiqueta = ['Entre 0 y 2', 'Entre 2 y 3', 'Entre 3 y 4', 'Entre 4 y 5']
                   
plt.title("Porcentajes por rating")
e = [0, 0, 0, 0.2]
plt.pie(rangos, labels=rangos_etiqueta, autopct='%1.1f%%', shadow=True, explode=e, startangle=180)
plt.axis('equal')
plt.show()


minifigs = df['minifigs'].dropna()
rango_minifigs = [int(m) for m in minifigs]
entre1y3 = 0  
entre4y6 = 0
entre7y9 = 0
mayor10 = 0

for i in rango_minifigs:
    if(i <= 3):
        entre1y3 = entre1y3 + 1
    elif(i <= 6 and i > 3):
        entre4y6 = entre4y6 + 1
    elif(i <= 9 and i > 6):
        entre7y9 = entre7y9 + 1
    else:
        mayor10 = mayor10 + 1

rangos = [entre1y3, entre4y6, entre7y9, mayor10]
rangos_etiqueta = ['De 1 a 3', 'De 4 a 6', 'De 7 a 9', 'Mayor a 10']
                   
plt.title("Numero de minifiguras en los productos")
e = [0, 0, 0, 0.2]
plt.pie(rangos, labels=rangos_etiqueta, autopct='%1.1f%%', shadow=True, explode=e, startangle=180)
plt.axis('equal')
plt.show()

# Productos mas comprados
plt.figure(figsize=(6,3))
plt.title("Productos mas comprados")
mas_comprados = df.sort_values('ownthisset',ascending=False)[:15]
y = mas_comprados["name"]
x = mas_comprados["ownthisset"]
plt.step(x,y)
plt.show()


ownthisset = df['ownthisset'].dropna()
rango_ownthisset = [int(m) for m in ownthisset]
hastamil = 0  
hasta3mil = 0
hasta6mil = 0
mayor6mil = 0

for i in rango_ownthisset:
    if(i <= 1000):
        hastamil = hastamil + 1
    elif(i <= 3000 and i > 1000):
        hasta3mil = hasta3mil + 1
    elif(i <= 6000 and i > 3000):
        hasta6mil = hasta6mil + 1
    else:
        mayor6mil = mayor6mil + 1

rangos = [hastamil, hasta3mil, hasta6mil, mayor6mil]
rangos_etiqueta = ['Menor a 1 000', '1 000 - 3 0000', '3 001 - 6 000', 'Mayor a 6 000']
                   
plt.title("Numero de compradores por los productos")
e = [0, 0.2, 0, 0.2]
plt.pie(rangos, labels=rangos_etiqueta, autopct='%1.1f%%', shadow=True, explode=e)
plt.axis('equal')
plt.show()


#productos LEGO
productoLEGO = df[df['name'].str.contains("LEGO", case=False)]

plt.figure(figsize=(6,3))
plt.title("Productos LEGO mas comprados")
mas_comprados = productoLEGO.sort_values('ownthisset',ascending=False)[:5]
x = mas_comprados["name"]
y = mas_comprados["ownthisset"]
plt.barh(x,y, edgecolor='black', color='Orange')
plt.show()

plt.figure(figsize=(6,3))
plt.title('Mayor Dificultad')
plt.xlabel("Número de piezas")
plt.ylabel("Producto")
mayor_numero_piezas_LEGO = productoLEGO.sort_values('pieces',ascending=False)[:5]
x=mayor_numero_piezas_LEGO["pieces"]
y=mayor_numero_piezas_LEGO["name"]
plt.scatter(x,y, s = (20*1)**2, color = ["orange","green","blue","yellow", "brown"], alpha=0.5)
plt.show()

plt.figure(figsize=(6,3))
plt.title('Puntuación de productos')
mayor_rating = productoLEGO.sort_values('rating',ascending=False)[:300]
mayor_rating.rating.value_counts().plot(kind='barh', color = "Red", alpha=0.5)
plt.show()
