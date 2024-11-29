#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:59:34 2024

@author: juanmanuelneiramantilla
"""

import pandas as pd

# Leer archivo CSV con punto y coma como delimitador
datos = pd.read_csv('Cuentas_por_cobrar_001.csv', encoding='latin-1', sep=';')
print(datos.head())
datos.set_index("Vendedor",inplace= True)
print("-----------------------ROSA MORAIDA ASUNCION CRUZ-----------------------")
print(datos.loc['ROSA MORAIDA ASUNCION CRUZ'])

print("-----------------------Redes Sociales  - RUT: 21123456 / Vendedor--------------------------")
print(datos.loc['ROSA MORAIDA ASUNCION CRUZ', 'Total'])