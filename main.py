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

print(f"Media por año:\n{dataframe.mean(numeric_only=True)}")

print(f"Varianza por año:\n{dataframe.var(numeric_only=True)}")


def calcular_moda(col):
    for i in col:
        d = dataframe[i].tolist()
        print(f"Moda año {i} {mode(d)}")


calcular_moda(columns)


def use_map(col):
    df = dataframe[col].map(lambda prod: prod * 1.20).tolist()
    print(df)


use_map("2019")


def values_greater_than_zero(col):
    df = dataframe[col]
    filt = filter(lambda prod: prod > 0, df)
    print(list(filt))


values_greater_than_zero("2020")


class Data_table:
    def __init__(self, sector):
        self.sector = sector

    def __str__(self):
        sector = self.info()
        return f"{self.sector} ha producido un total por año de: {str(sector)}"

    def info(self):
        sectores = dataframe["Producción"].tolist()
        index = sectores.index(self.sector)
        columnas = columns.delete(0)
        tuple = []
        sector = {}
        for i in columnas:
            sector[str(i)] = dataframe[str(i)][index]
            tuple.append(dataframe[str(i)][index])
        return sector, tuple

    def __gt__(self, other):
        result, _ = self.info()
        if result.get("2021") > other:
            return -1

    def __eq__(self, other):
        result, _ = self.info()
        if result.get("2021") == other:
            return 0

    def __lt__(self, other):
        result, _ = self.info()
        if result.get("2021") < other:
            return 1

    def __add__(self, other):
        result, _ = self.info()
        return result.get("2021") + other

    def __sub__(self, other):
        result, _ = self.info()
        return result.get("2021") - other


pesca = Data_table("        03 Pesca y acuicultura")
manufacturera = Data_table("        C Industria manufacturera")
papel = Data_table("        17 Industria del papel")
agricultura = Data_table("        A Agricultura, ganadería, silvicultura y pesca")
quimica = Data_table("        20 Industria química")

lista_sectores = [pesca, manufacturera, papel, agricultura, quimica]
for ls in lista_sectores:
    info, _ = ls.info()
    info = info.get("2021")
    print(ls.__gt__(info))
    print(ls.__lt__(info))
    print(ls.__eq__(info))
    print(ls.__sub__(info))
    print(ls.__add__(info))
    print("-------------")


def converter(data):
    numbers = []
    for x in data:
        numbers.append(int(x))
    return numbers


fig, ax = pp.subplots()
_, ax2 = pp.subplots()
_, ax3 = pp.subplots()

years = columns.delete(0)
pesca = Data_table("        03 Pesca y acuicultura")
_, prod = pesca.info()
lista = converter(prod)
ax.plot(years, prod, color='red')
pp.savefig('grafico.png')
ax2.scatter(years, prod)
ax3.bar(years, prod)
pp.show()


con = sqlite3.connect("produccion.db")

table = dataframe.to_sql(name="Produccion", con=con)


