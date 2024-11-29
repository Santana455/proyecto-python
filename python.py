#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:21:17 2024

@author: juanmanuelneiramantilla
"""

import pandas as pd

# Leer archivo CSV con punto y coma como delimitador
datos = pd.read_csv('Cuentas_por_cobrar_001.csv', encoding='latin-1', sep=';')

# Mostrar información básica del DataFrame
print(datos.info())
print(datos.head())  # Primeras 5 filas para inspecció
print('\n' * 2)

# Mostrar las primeras 19 filas
print(datos.iloc[0:19])
print('\n' * 2)

# Mostrar renglones salteados
print(datos.iloc[[0, 3, 6, 24, 50, 45]])

# Mostrar las dos primeras columnas
print(datos.iloc[:, 0:2])
# Mostrar filas y columnas seleccionadas salteado
print((datos.iloc[[0,3,6,24], [0,2,4]]))
# Mostrar rangos de reglones y columnas continuos
print(datos.iloc[0:5,5:8])