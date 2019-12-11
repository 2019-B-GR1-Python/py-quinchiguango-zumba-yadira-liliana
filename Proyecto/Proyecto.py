# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 09:45:55 2019

@author: Yadira Quinchiguango
"""

import pandas as pd

import matplotlib.pyplot as plt


path = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto//dataset.csv"
df= pd.read_csv(path, encoding = 'unicode_escape',sep = ";")
             
asesinato_genero = pd.crosstab(df.TipoMuerte, df.Genero)

plt.figure(figsize=(6,3))
plt.title('Homicidios por Genero')
df.Genero[df.TipoMuerte=="Homicidios"].value_counts().sort_values().plot(kind='bar')
plt.savefig("C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto//AsesinatosEdad.jpg")
plt.show()

plt.figure(figsize=(6,3))
plt.title('Asesinatos por Genero')
df.Genero[df.TipoMuerte=="Asesinatos"].value_counts().sort_values().plot(kind='barh')
plt.show()

plt.figure(figsize=(6,3))
plt.title('Tipo de Muerte')
df.TipoMuerte.value_counts().sort_values().plot(kind='barh')
plt.savefig("C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto//tipoMuerte.jpg")
plt.show()

plt.figure(figsize=(6,3))
plt.title('Provincias con mas muertes')
df.Provincia.value_counts()[:5].sort_values().plot(kind='barh')
plt.savefig("C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto//ProvinciaMasAsesinatos.jpg")
plt.show()
 
plt.figure(figsize=(6,3))
plt.title('Ciudades con mas muertes')
df.Canton.value_counts()[:5].sort_values().plot(kind='barh')
plt.savefig("C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//Proyecto//PLugarMasAsesinatos.jpg")
plt.show()

pd.crosstab(df.Genero, df.EstadoCivil)
pd.crosstab(df.TipoMuerte.where(df.TipoMuerte=="Femicidios"), df.EstadoCivil)

edad = df['Edad'].dropna()
rango_edades = [int(e) for e in edad]
menores20 = 0 
menores40 = 0 
menores60 = 0
mayores60 = 0
for i in rango_edades:
    if(i <= 20):
        menores20 = menores20 + 1
    elif(i <= 40 and i > 20):
        menores40 = menores40 + 1
    elif(i <= 60 and i > 40):
        menores60 = menores60 + 1
    else:
        mayores60 = mayores60 + 1

edades = [menores20, menores40, menores60, mayores60]
edades_etiqueta = ['Menores a 20 años', 'Entre 20 y 40 años', 'Entre 40 y 60 años', 'Mayores a 60 años']
                   
plt.title("Muertes por edad")
plt.pie(edades, labels=edades_etiqueta, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

edad = df.Edad[df.TipoMuerte=="Asesinatos"].dropna()
rango_edades = [int(e) for e in edad]
menores20 = 0 
menores40 = 0 
menores60 = 0
mayores60 = 0

for i in rango_edades:
    if(i <= 20):
        menores20 = menores20 + 1
    elif(i <= 40 and i > 20):
        menores40 = menores40 + 1
    elif(i <= 60 and i > 40):
        menores60 = menores60 + 1
    else:
        mayores60 = mayores60 + 1

edades = [menores20, menores40, menores60, mayores60]
edades_etiqueta = ['Menores a 20 años', 'Entre 20 y 40 años', 'Entre 40 y 60 años', 'Mayores a 60 años']
                   
plt.title("Muertes por edad")
plt.pie(edades, labels=edades_etiqueta, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

edad = df.Edad[df.Provincia=="PICHINCHA"].dropna()
rango_edades = [int(e) for e in edad]
menores20 = 0 
menores40 = 0 
menores60 = 0
mayores60 = 0

for i in rango_edades:
    if(i <= 20):
        menores20 = menores20 + 1
    elif(i <= 40 and i > 20):
        menores40 = menores40 + 1
    elif(i <= 60 and i > 40):
        menores60 = menores60 + 1
    else:
        mayores60 = mayores60 + 1

edades = [menores20, menores40, menores60, mayores60]
edades_etiqueta = ['Menores a 20 años', 'Entre 20 y 40 años', 'Entre 40 y 60 años', 'Mayores a 60 años']
                   
plt.title("Muertes por edad")
plt.pie(edades, labels=edades_etiqueta, autopct='%1.1f%%')
plt.axis('equal')
plt.show()