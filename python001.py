#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:14:57 2024

@author: juanmanuelneiramantilla
"""

import pandas as pd

# Leer archivo CSV con punto y coma como delimitador
datos = pd.read_csv('Cuentas_por_cobrar_001.csv', encoding='latin-1', sep=';')
print(datos.head())
datos.set_index("Cliente",inplace= True)
print("-----------------------MILAGROS PUCLLA - RUT: 94586891-----------------------")
print(datos.loc['MILAGROS PUCLLA - RUT: 94586891'])

print("-----------------------       POSTURA  VEGA - RUT: 250102021 / Total-----------------------")
print(datos.loc['POSTURA  VEGA - RUT: 250102021', 'Total'])

print("-----------------------GROVER VEGA  - RUT: 21123456 / Vendedor / Total--------------------------")
print(datos.loc['GROVER VEGA  - RUT: 21123456', ['Vendedor', 'Total', 'Importe adeudado']])

print(("----------------------------------------SELECCION AMPLIA----------------------------------------------"))
print(datos.loc[['GROVER VEGA  - RUT: 21123456','DELEITE  RESTAURANTE - RUT: 69715403'],['Vendedor','Total']])

print("----------------------------------------SELECCION CON RANGO-------------------------------------------------")
print(datos.loc[['ROMEL FRANKLIN - RUT: 1234877', 'JULCA - RUT: CL000066'], 'Total':'Estado'])

print("----------------SELECCION CUALQUIER COLUMNAS, SELECCION DE FILAS FILTRANDO CON LA ULTIMA PALABRA---------------------")
print(datos.loc[datos['Vendedor'].str.endswith("Sociales")])

