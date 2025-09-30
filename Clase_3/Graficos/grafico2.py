import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Varga\OneDrive\Desktop\Santiago\Clase_3\Segmentación\Usuarios_segmentados.csv")
plt.figure(figsize=(12,5))

plt.subplot(2,2,1)
sns.countplot(data=df, x="segmento_clicks", hue="suscripcion", palette="pastel")
plt.title("Usuarios por segmento de clicks")

#barras
plt.subplot(2,2,2)
df['suscripcion'].value_counts().plot(kind = 'bar')
plt.title("BD")

#bigotes
plt.subplot(2,2,3)
sns.boxplot(data=df, x="suscripcion", y="compras", palette="muted")
plt.title("Destribución de compras según suscripciones")

#mapa calor
plt.subplot(2,2,4)
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm",)
plt.title("Mapa de calor de correlaciones")


plt.tight_layout()
plt.show()

