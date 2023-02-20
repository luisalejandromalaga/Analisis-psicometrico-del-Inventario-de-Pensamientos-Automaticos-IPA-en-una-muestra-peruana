# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:57:16 2022

@author: User
"""


"""Paquetería"""
import numpy as np
import pandas as pd
import math

datos =  pd.read_excel('data_uno.xlsx')


data = datos.dropna(axis='rows')


data.to_excel('data_uno_limpia.xlsx', index = False)