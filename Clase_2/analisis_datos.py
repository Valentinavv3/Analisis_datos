import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("usuarios_app_limpio.csv", encoding = "utf-8")


total_usuarios = len(df)
print("Total de usuarios limpios", total_usuarios)


stats = (
    df.groupby(["pais","estado",])["tiempo_sesion_min"] 
    .agg(["mean","median","count"]) 
    .rename(columns={"mean":"promedio", "median":"mediana","count":"cantidad"})
    .reset_index()
)
print("\n Estadisticas  por pais y estado:")
print(stats)


correlacion = df["edad"].corr(df["clicks"])
print("\nCorrelacion entre edad y clicks",correlacion)

plt.figure(figsize=(10,5))
usuarios_por_pais = df.groupby("pais")["usuario_id"].count().reset_index()
sns.barplot(data=usuarios_por_pais,x="pais", y="usuario_id", hue="pais", palette="viridis")

plt.title('Usuarios por Pais')
plt.xlabel('pais')
plt.ylabel('Cantidad de usuarios')
plt.show()


plt.figure(figsize=(8,4))
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm",)
plt.title("Mapa de calor de correlaciones")
plt.tight_layout()
plt.show()