import pandas as pd
from numpy import var
from statistics import mode
from matplotlib import pyplot as pp
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


print(data_to_tupla(columns))
print('\n')
print(data_to_dic(columns))


def concat_and_save(nombre, data):
    file = open(nombre, "wt")
    for values in data:
        file.write(f"{values[1]}  {values[2]}\n")
    print("Fichero creado e info almacenada correctamente.")


concat_and_save("lista.txt", data_to_tupla(columns))

dataframe2 = pd.read_excel(excel_file, sheet_name="tabla-32449")
cambio_filas_columnas = dataframe2.transpose()
print(cambio_filas_columnas)

print(f"Media por año:\n{dataframe.mean()}")

print(f"Varianza por año:\n{dataframe.var()}")


def calcular_moda(col):
    for i in col:
        d = dataframe[i].tolist()
        print(f"Moda año {i} {mode(d)}")


calcular_moda(columns)

