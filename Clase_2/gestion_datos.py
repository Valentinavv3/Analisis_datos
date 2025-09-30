import pandas as pd 
import numpy as np 
import re

df = pd.read_csv("Clase_2/Usuarios_app_clase2.csv", encoding="utf-8")


df.columns = (df.columns.str.strip()
            .str.lower()
            .str.replace(" ","_",regex=False))


map_pais = {"mexico":"México",
            "méxico":"México",
            "Mexico":"México"}

df['pais']=df['pais'].astype(str).str.strip().replace(map_pais)

def to_number(x):
    if pd.isna(x) or str(x).strip() == "":

        return np.nan
    
    h = str(x).strip().lower()
    palabras ={"quince":15}
    if h in palabras:
        return float(palabras[h])
    s = re.search(r"(\d+)", h) 
    
    return float(s.group(1)if s else np.nan)
    

df ["edad"] = df["edad"].apply(to_number)
df ["tiempo_sesion_min"] = df["tiempo_sesion_min"].apply(to_number)
df ["clicks"] = df["clicks"].apply(to_number)
df ["compras"] = df["compras"].apply(to_number)


df = df.drop_duplicates(subset=["nombre","edad","pais","tiempo_sesion_min","estado","suscripcion","clicks","compras"])


df= df.dropna(subset=["edad","tiempo_sesion_min"])


df= df[df["edad"].between(10,100)]
df = df[df["tiempo_sesion_min"].between(10,100)]


df.to_csv("usuarios_app_limpio.csv",index=False,encoding="utf-8") 
print("Limpieza finalizada. Filas:", df.shape[0])