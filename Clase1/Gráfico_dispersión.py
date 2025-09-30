import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("usuarios_app_limpieza.csv")


df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['tiempo sesión'] = pd.to_numeric(df['tiempo sesión'], errors='coerce')


df = df.dropna(subset=['edad', 'tiempo sesión'])


df = df[df['estado'] == 'activo']


sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))


sns.scatterplot(
    data=df,
    x='edad',
    y='tiempo sesión',
    hue='país',          
    palette='pastel',
    edgecolor="black",
    s=80
)


plt.title('Relación entre Edad y Tiempo de Sesión (Usuarios Activos)')
plt.xlabel('Edad')
plt.ylabel('Tiempo de Sesión')


plt.tight_layout()
plt.show()
