import pandas as pd
import random

nombres = [
    "Valentina", "Mateo", "Isabella", "Santiago", "Mariana", "Sebastián", 
    "Camila", "Samuel", "Gabriela", "Juan", "Laura", "Andrés", "Natalia",
    "Felipe", "Sara", "Daniel", "Lucía", "Tomás", "Paula", "David", 
    "Carolina", "Nicolás", "Martina", "Julián", "Emilia", "Alejandro", 
    "Florencia", "Miguel", "Antonia"
]

paises = ["Colombia", "Barcelona", "Ecuador", "México", "Argentina"]

suscripciones = ["Free", "Premium"]

estados = ["Activo", "Inactivo"]

data = []

for i in range(1, 201):
    nombre = random.choice(nombres)
    edad = random.randint(18, 60)
    pais = random.choice(paises)
    tiempo = random.randint(5, 200)
    estado = random.choice(estados)
    suscripcion = random.choice(suscripciones)
    clicks = random.randint(10, 300)
    compras = random.randint(0, 5)

    data.append({
        "usuarios_id": i,
        "nombre": nombre,
        "edad": edad,
        "pais": pais,
        "tiempo": tiempo,
        "estado": estado,
        "suscripcion": suscripcion,
        "clicks": clicks,
        "compras": compras
    })

df = pd.DataFrame(data, columns=["usuarios_id", "nombre", "edad", "pais", "tiempo", "estado", "suscripcion", "clicks", "compras"])

# Exportar a Excel y CSV
df.to_excel("Usuarios.xlsx", index=False)
df.to_csv("Usuarios.csv", index=False, encoding="utf-8")
