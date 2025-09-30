import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("usuarios_app.csv")

df['pais'].value_counts().plot(kind = 'bar')

plt.title('Usuarios por pais')
plt.xlabel('Pais')
plt.ylabel('Cantidad de Usuarios')
plt.show()