#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:38:14 2024

@author: juanmanuelneiramantilla
"""

import pandas as pd

# Leer archivo CSV con punto y coma como delimitador
datos = pd.read_csv('Cuentas_por_cobrar_001.csv', encoding='latin-1', sep=';')
df = pd.DataFrame(datos)

df.reset_index().to_csv('DatosExportadosCuentas_por_cobrar_001.csv', header= True,
                        index=False)

datos.set_index("Vendedor",inplace= True)
print("-----------------------ROSA MORAIDA ASUNCION CRUZ-----------------------")
print(datos.loc['ROSA MORAIDA ASUNCION CRUZ'])

df.reset_index().to_csv('DatosExportadosCuentas_por_cobrar_001.csv', header= True,
                        index=False)
