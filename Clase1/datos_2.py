import pandas as pd

#cargar los datos
df = pd.read_csv("usuarios_app_limpieza.csv")

#comando solo para ver las primeras filas
print(df.head())

#ver info general de la BD
print(df.info())

#comando para ver estadisticas basicas
print(df.describe())

#limpieza de datos
df = df.drop_duplicates(subset=['nombre','edad','pais','tiempo sesion','estado']) #datos repetidos

#rellenar el dato con el promedio
df['edad'] = df['edad'].fillna(df['edad'].mean()) #datos nulos

#filtrar usuarios activos
usuarios_activos = df[df['estado'] == 'activo']
