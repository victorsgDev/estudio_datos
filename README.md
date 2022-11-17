# JUPYTER NOTEBOOK ADJUNTADO : VictorsgDev
Realizar un estudio de datos con los siguientes pasos:
- Utilizando python descarga un archivo tipo excel con datos estadísticos del
INE. Puedes elegir el tema que quieras, pero tiene que tener al menos 30
filas y 100 datos (las columnas deben ser años, meses o días)
- Carga los datos en una variable y crea un dataset con ellos. Necesitarás el
nombre de la hoja y la fila y columna en que están los nombres, también
deberás guardar los datos de las primeras celdas para los títulos de los
gráficos (hasta que empiezan las columnas con los años – meses - días) y
luego eliminar esas filas para evitar errores

- Si hay celdas sin valor (sd, NaN,…), conviértelos a 0. Comprueba si hay datos
que no deberían estar ahí (valores menores que cero sin sentido, texto en
celdas numéricas, o números en celdas de texto). Tendrás que hacer una o
varias funciones que lo comprueben
- A partir del dataset, crea una colección de datos de cada tipo estudiado
utilizando una fila distinta.
- Concatena todos los datos de la lista utilizando espacios entre medias y
guárdalo en un fichero de texto con el nombre “lista.txt”
- Crea una función que cambie las filas por columnas para tener el dataset con
los años (meses o días) en las filas
- Crea una función que recorra las columnas y calcule la media, la varianza y la
moda de cada una.
- Utiliza map para crear una función que haga algo con el dataset
- Utilizar filter para crear una función que extraiga un sub-dataset
- Crea una clase que tenga como atributos las columnas
- Define una forma de imprimir los objetos de la clase en la que aparezcan
todos los datos de la clase
- Crea métodos para modificar el valor de cada atributo
- Redefine los métodos especiales de comparación para poder comparar los
objetos de la clase por el valor de la segunda columna y los de la suma y resta
para que devuelvan el valor de la suma o resta de cada atributo
- Crea un objeto de la clase para al menos cinco filas y prueba todos tus
métodos
- Realiza gráficos anuales (mensuales o diarios) para cada columna, por grupos
de dos columnas, tres columnas y todas las columnas juntas. Los gráficos
deben ser de distintos tipos
- Crea una base de datos SQLite desde python
- Guarda el dataset como una tabla en la base de datos
- Realiza al menos tres consultas distintas
- Guarda los datos de una de las consultas en un nuevo dataset
- Guarda el nuevo dataset como una nueva tabla en la base de datos