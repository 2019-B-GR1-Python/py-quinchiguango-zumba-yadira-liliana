# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:50:09 2019

@author: yadira
"""

import pandas as pd
path_guardado_bin="C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data_full.pickle"
df=pd.read_pickle(path_guardado_bin)

# Obtener los nombres de los artistas
serie_artistas_repetidos = df["artist"]

# Obtener los nombres no repetidos de cada artistas
artistas= pd.unique(serie_artistas_repetidos)

#longitus del arreglo
artistas.size
len(artistas)

# Obtener solo las obras del artista BLAKE, William
blake = df["artist"]=='Blake, William'

# Filtra en el mismo orden las obras de blake
df_blake = df[blake]
df_blake = df[blake]['title']
blake_unicos = pd.unique(df_blake)

blake.value_counts() #indica cuantos hay de cada uno
df["artist"].value_counts()