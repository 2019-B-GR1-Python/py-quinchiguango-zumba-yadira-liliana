# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:17:52 2020

@author: yadir
"""

import pandas as pd
import numpy as np
import math

path_guardado_bin="C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data_full.pickle"
df=pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()
# no tenga referencias y sea una seccion completamente nueva

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)

for columna_agrupada,df_completo in df_agrupado:
    print(type(columna_agrupada)) #str
    print(type(df_completo)) #Dataframe
    
for acquisitionYear, registros in df_agrupado:
    print(acquisitionYear)

serie_unidades = seccion_df['units'].value_counts()
serie_unidades.empty #Saber si esta vacio
    
def llenar_valores_vacios(series, tipo): # TIPO: Repetido(value_counts) / Promedio
    lista_valores = series.value_counts()
    if (lista_valores.empty == True):
        return  series
    else:
        if(tipo == 'promedio'):
            suma = 0
            num_elementos = 0
            for valor_str in series:
                valor = float(valor_str)
                condicionNoVacio = math.isnan(valor)
                if (condicionNoVacio):
                    pass
                else:
                    num_elementos += 1
                    suma = suma + valor

            promedio = suma/ num_elementos
            # Busca los nan y pone el valor que se le mande
            serie_valores_llenos = series.fillna(promedio)
            return serie_valores_llenos
        elif (tipo == 'value_counts'):
            valor_repetido = lista_valores.keys().tolist()
            serie_valores_llenos = series.fillna(valor_repetido[0])
            return serie_valores_llenos
            
#Agrupamos por artista para tener valores mas coherentes de las distintas columnas        
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    for atista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'value_counts')
        lista_df.append(copia)
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

df_transformado = transformar_df(seccion_df)               