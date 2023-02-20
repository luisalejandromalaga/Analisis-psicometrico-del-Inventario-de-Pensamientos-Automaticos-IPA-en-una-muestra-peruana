# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:18:26 2022

@author: User
"""

"""Paquetería"""
import numpy as np
import pandas as pd

datos =  pd.read_excel('data_dos.xlsx')

t1 = {}#Array vacio

for col in datos.columns[2:47]:
    row = []#aaray vacion
    for i in datos[col]:
        if i == "Nunca pienso eso" : row.append(0)
        if i == "Algunas veces lo pienso" : row.append(1)
        if i == "Bastantes veces lo pienso" : row.append(2)
        if i == "Con mucha frecuencia lo pienso" : row.append(3)             
    t1[col] = row  
   
t1_key = pd.DataFrame(t1.keys())
t1_key.columns = ['key']

#Pasamos el diccionario a DataFrame, aunque se devuelve girado por lo que lo rotamos d.T
d = pd.DataFrame.from_dict(t1, orient='index')
test = d.T


#Juntar
db = [ datos['Edad'], datos['Sexo'], test  ]
datos_export = pd.concat(db, axis=1)
datos_export.to_excel('data_dos_limpia.xlsx', index = False)