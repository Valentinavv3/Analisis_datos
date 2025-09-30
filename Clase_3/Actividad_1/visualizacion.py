import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ACTIVIDAD 3: VISUALIZACIÓN DE DATOS


clientes = pd.read_csv("clientes.csv")
productos = pd.read_csv("productos.csv")
ventas = pd.read_csv("ventas.csv")

df = ventas.merge(clientes, on="id_cliente").merge(productos, on="id_producto")

df["valor_total"] = df["cantidad"] * df["precio"]


# 1. Grafica el gasto total por ciudad en un gráfico de barras.
gasto_ciudad = df.groupby("ciudad")["valor_total"].sum().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=gasto_ciudad, x="ciudad", y="valor_total")
plt.title("Gasto total por ciudad")
plt.show()

# 2. Grafica los productos más vendidos (cantidad total de cada producto).
productos_vendidos = df.groupby("producto")["cantidad"].sum().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=productos_vendidos, x="producto", y="cantidad")
plt.title("Productos más vendidos")
plt.show()

# 3. Haz un gráfico de caja (boxplot) para analizar la distribución del gasto por ciudad.
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="ciudad", y="valor_total")
plt.title("Distribución del gasto por ciudad")
plt.show()
