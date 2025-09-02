# importar librerías
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# leer el archivo CSV
df = pd.read_csv("usuarios_app_limpieza.csv")

# convertir edad y tiempo_seccion a números (lo inválido se vuelve NaN)
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['tiempo sesión'] = pd.to_numeric(df['tiempo sesión'], errors='coerce')

# quitar filas donde falte edad o tiempo_seccion
df = df.dropna(subset=['edad', 'tiempo sesión'])

# filtrar solo los usuarios activos
df = df[df['estado'] == 'activo']

# estilo del gráfico
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# crear scatterplot
sns.scatterplot(
    data=df,
    x='edad',
    y='tiempo sesión',
    hue='país',          
    palette='pastel',
    edgecolor="black",
    s=80
)

# título y etiquetas
plt.title('Relación entre Edad y Tiempo de Sesión (Usuarios Activos)')
plt.xlabel('Edad')
plt.ylabel('Tiempo de Sesión')

# mostrar gráfico
plt.tight_layout()
plt.show()
