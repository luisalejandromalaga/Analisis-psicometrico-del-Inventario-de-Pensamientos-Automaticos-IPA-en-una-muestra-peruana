# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:23:04 2022

@author: User
"""

"""Paquetería"""
import numpy as np
import pandas as pd
import math

datos =  pd.read_excel('data_tres.xlsx')


data = datos.dropna(axis='rows')


data.to_excel('data_tres_limpia.xlsx', index = False)