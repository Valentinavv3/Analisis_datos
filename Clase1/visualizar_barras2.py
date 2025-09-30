import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns # patra usar la paleta

df = pd.read_csv("usuarios_app.csv")

#obtener los conteos de pais
conteos = df['pais'].value_counts()

# crear la paleta de colores (pastel)
colors = sns.color_palette("pastel", len(conteos))

#graficar con colores personalizados
ax = conteos.plot(kind = 'bar', color=colors)

#titulo y etiquetas
plt.title('Usuarios por pais')
plt.xlabel('Pais')
plt.ylabel('Cantidad de Usuarios')

plt.show()