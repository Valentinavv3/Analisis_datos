import pandas as pd

#cargar los datos
df = pd.read_csv("usuarios_app.csv")

#comando solo para ver las primeras filas
print(df.head())

#ver info general de la BD

print(df.info())

#comando para ver estadisticas basicas
print(df.describe())
