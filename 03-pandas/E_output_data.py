# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:58:11 2019

@author: yadira
"""

import pandas as pd
import os
import sqlite3
import xlsxwriter

path_guardado_bin = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data_full.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50019,:].copy()

# Tipos archivos
# 1)JSON
# 2)EXCEL
# 3)SQL

# EXCEL
path_excel  = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//mi_df_completo.xlsx"
df.to_excel(path_excel, index = False)
columnas =["artist","title", "year"]
df.to_excel(path_excel, columns= columnas ,index = False)


# - Multiples hojas de trabajo (en Excel)
#Se crea una instancia de pandas  excel weriter
path_excel_multiple  ="C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//mi_df_multiple.xlsx"
writer = pd.ExcelWriter(path_excel_multiple , engine="xlsxwriter")
#definicion de hojas excel
df.to_excel(writer, sheet_name="Primera")
df.to_excel(writer, sheet_name="Segunda", index= False)
df.to_excel(writer, sheet_name="Tercera", columns= columnas)

writer.save()

#Colores
#Conteo de numero de artistas
num_artistas = df['artist'].value_counts()
path_excel_colores  = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//mi_df_colores.xlsx"
writer_colores = pd.ExcelWriter(path_excel_colores , engine="xlsxwriter")

num_artistas.to_excel(writer_colores,sheet_name='Artistas')
num_artistas.to_excel(writer_colores,sheet_name='Grafico')

#Guardamos temporalmente la hoja de artistas para trabajar en ella
hoja_artistas  = writer_colores.sheets['Artistas']
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)
formato_artistas={
        "type":"2_color_scale",
        "min_value":"10",
        "min_type": "percentile",
        "max_value":"99",
        "max_type":"percentile"
        }
hoja_artistas.conditional_format(rango_celdas,formato_artistas)

writer_colores.save()

# EJEMPLO

## Grafico
workbook = writer_colores.book
worksheet = writer_colores.sheets['Grafico']
chart = workbook.add_chart({'type': 'column'})
writer_colores.save()

################# EXPORTAR DATOS A SQL Y JSON #################

import numpy as np
import pandas as pd
import os
import sqlite3

with sqlite3.connect("C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//bdd_artist.db") as conexion:
    df5.to_sql('py_artistas', conexion)

###  JSON ####
df.to_json('C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artistas.json')

### json con formato aceptable: orientado a tabla ###
df.to_json('C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artistas_tabla.json', orient='table')