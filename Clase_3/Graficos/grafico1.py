import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Varga\OneDrive\Desktop\Santiago\Clase_3\Segmentación\Usuarios_segmentados.csv")
plt.figure(figsize=(12,5))
plt.subplot(2,2,1)
sns.countplot(data=df, x="segmento_clicks", hue="suscripcion", palette="pastel")
plt.title("Usuarios por segmento de clicks")
plt.subplot(1,2,2)

sns.boxplot(data=df, x="suscripcion", y="compras", palette="mute")
plt.title("Destribución de compras según suscripciones")
plt.tight_layout()
plt.show()

