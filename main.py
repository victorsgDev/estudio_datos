import pandas as pd
from numpy import var
from statistics import mode
from matplotlib import pyplot
import sqlite3

# Enlace : https://www.ine.es/jaxiT3/files/t/es/xls/32449.xls?nocab=1
excel_file = pd.ExcelFile('resources/file.xlsx')
dataframe = pd.read_excel(excel_file, sheet_name="tabla-32449")
columns = dataframe.columns
dataframe = dataframe.fillna(0)
dataframe = dataframe.replace({'..': 0})


def comprobar_valor_celdas():
    columnas = columns.delete(0)
    for c in columnas:
        c = str(c)
        for celda in dataframe[c]:
            if celda < 0:
                dataframe.replace({celda: 0})


comprobar_valor_celdas()


def data_to_tupla(col):
    tupla_silvicultura = []
    col = col.delete(0)
    for column in col:
        c = str(column)
        tupla_silvicultura.append(("sector_silvicultura", c, dataframe[c][4]))

    return tupla_silvicultura


def data_to_dic(col):
    dic_agricultura = []
    col = col.delete(0)
    for column in col:
        c = str(column)
        dic_agricultura.append(("sector_agricultura", c, dataframe[c][1]))


print(data_to_dic(columns))
print(data_to_tupla(columns))
