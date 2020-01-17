# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:34 2019

@author: yadir
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML
# 2) Binary files -> (!#mf-.123'120)
# 3) Bases de datos Relacionales

columnas = ['id','artist','title','medium','year',
            'acquisitionYear', 'height',
            'width', 'units']

path = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data.csv"
df1 = pd.read_csv(path,nrows=10)
df2 = pd.read_csv(path,nrows=10,usecols = columnas)
df3 = pd.read_csv(path,nrows=10,usecols = columnas,
                  index_col = 'id')
df4 = pd.read_csv(path)

#Guardar un respaldo
path_guardado = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data.pickle"
df3.to_pickle(path_guardado)

path_guardado_bin = "C://Users//yadir//Documents//GitHub//py-quinchiguango-zumba-yadira-liliana//03-pandas//data//artwork_data_full.pickle"
df4.to_pickle(path_guardado_bin)

df5 = pd.read_pickle(path_guardado)





