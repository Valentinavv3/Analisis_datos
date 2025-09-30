import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ACTIVIDAD 1: CARGAR Y EXPLORAR LA BASE DE DATOS

# 1. Crea tres tablas

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4, 5],
    "nombre": ["Ana", "Carlos", "Luisa", "Pedro", "Valentina"],
    "edad": [25, 34, 29, 40, 22],
    "ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá", "Medellín"]
})

productos = pd.DataFrame({
    "id_producto": [101, 102, 103, 104],
    "producto": ["Laptop", "Celular", "Tablet", "Audífonos"],
    "precio": [3500, 2500, 1500, 500]
})

ventas = pd.DataFrame({
    "id_venta": [1, 2, 3, 4, 5, 6, 7],
    "id_cliente": [1, 2, 1, 3, 4, 5, 2],
    "id_producto": [101, 102, 104, 103, 101, 102, 104],
    "cantidad": [1, 2, 3, 1, 1, 2, 4]
})

# 2. Guarda cada tabla como un archivo CSV con to_csv().
clientes.to_csv("clientes.csv", index=False)
productos.to_csv("productos.csv", index=False)
ventas.to_csv("ventas.csv", index=False)

# 3. Carga de nuevo los tres archivos con pd.read_csv() para simular que vienen de fuentes externas.
clientes = pd.read_csv("clientes.csv")
productos = pd.read_csv("productos.csv")
ventas = pd.read_csv("ventas.csv")

# 4. Explorar datos
print("Clientes:\n", clientes.head(), "\n")
print("Productos:\n", productos.head(), "\n")
print("Ventas:\n", ventas.head(), "\n")

print("Estadísticas clientes:\n", clientes.describe(), "\n")
print("Estadísticas productos:\n", productos.describe(), "\n")
print("Estadísticas ventas:\n", ventas.describe(), "\n")




