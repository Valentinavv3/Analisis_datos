import pandas as pd

# ACTIVIDAD 2: SEGMENTACIÓN DE CLIENTES

clientes = pd.read_csv("clientes.csv")
productos = pd.read_csv("productos.csv")
ventas = pd.read_csv("ventas.csv")

# 1. Une las tablas de ventas con clientes y productos usando merge().
df = ventas.merge(clientes, on="id_cliente").merge(productos, on="id_producto")

# 2. Crea una nueva columna llamada valor_total multiplicando la cantidad por el precio del producto.
df["valor_total"] = df["cantidad"] * df["precio"]

#3. Agrupa por cliente (groupby) para calcular el gasto total de cada uno.
gasto_clientes = df.groupby(["id_cliente", "nombre"])["valor_total"].sum().reset_index()

# 4. Crea una columna de segmentación usando pd.cut()
gasto_clientes["segmento"] = pd.cut(
    gasto_clientes["valor_total"],
    bins=[0, 2000, 5000, 10000],
    labels=["Bajo", "Medio", "Alto"]
)
# 5. Muestra el resultado con el nombre del cliente, su gasto total y su segmento.
print("\n--- Segmentación de clientes ---")
print(gasto_clientes)

