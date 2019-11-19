# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:46 2019

@author: yadira
"""
import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)
serie_d = pd.Series([
        True, 
        False, 
        12, 
        12.12,
        "Yadira",
        None,
        (),
        [],
        {"nombre":"Adrian"}
        ])
serie_d[3]

lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]
serie_ciudad = pd.Series(lista_ciudades,
                         index=[
                                 "A",
                                 "C", 
                                 "L",
                                 "Q",
                                 ])



