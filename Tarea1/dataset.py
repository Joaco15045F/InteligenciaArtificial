import pandas as pd

archivo_dataset = pd.read_csv("cars_2010_2020.csv")
print(archivo_dataset)


#Analisis
#Mostrar 10 primeras filas
print("10 primeras filas")
print(archivo_dataset.head(10))

#Informacion del dataset
print("Informacion del Dataset")
print(archivo_dataset.info())


#Estadistica Descriptiva
print("Estadistica")
print(archivo_dataset.describe(include="all"))

desc_stats = archivo_dataset.describe(include="all")
desc_stats.to_csv("estadistica.csv")


#valores unicos en cada columna
print("valores unicos por columna")
print(archivo_dataset.nunique())


