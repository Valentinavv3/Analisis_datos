import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("usuarios_app_limpieza.csv")


df = df.dropna(subset=['edad'])


colors = sns.color_palette("pastel", len(df['país']))

# graficar boxplot
ax = sns.boxplot(x="país", y="edad", data=df, palette=colors)


plt.title('Distribución de edad por país')
plt.xlabel('País')
plt.ylabel('Edad')

plt.show()



