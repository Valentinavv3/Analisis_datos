import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# cargar los datos
df = pd.read_csv("usuarios_app_limpieza.csv")

# eliminar filas donde la edad esté vacía
df = df.dropna(subset=['edad'])

# crear la paleta de colores (pastel)
colors = sns.color_palette("pastel", len(df['país']))

# graficar boxplot con colores personalizados
ax = sns.boxplot(x="país", y="edad", data=df, palette=colors)

# titulo y etiquetas
plt.title('Distribución de edad por país')
plt.xlabel('País')
plt.ylabel('Edad')

plt.show()
