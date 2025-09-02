import pandas as pd

df = pd.read_csv("usuarios_app_limpieza.csv")  

# Eliminar duplicados
df = df.drop_duplicates(subset=['nombre', 'edad', 'país', 'tiempo sesión', 'estado'])

# Eliminar registros sin edad
df = df.dropna(subset=['edad'])

# Asegurar columnas numéricas
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['tiempo sesión'] = pd.to_numeric(df['tiempo sesión'], errors='coerce')

# Eliminar filas donde edad o tiempo sesión no sean válidos
df = df.dropna(subset=['edad', 'tiempo sesión'])


# 1 punto por cada minuto de sesión
df['XP'] = df['tiempo sesión']

# 10 puntos extra si el usuario está activo
df['XP'] += df['estado'].apply(lambda x: 10 if str(x).lower() == 'activo' else 0)


def asignar_nivel(xp):
    if xp < 20:
        return "Novato"
    elif 20 <= xp <= 39:
        return "Intermedio"
    elif 40 <= xp <= 59:
        return "Avanzado"
    else:
        return "Experto"

df['nivel'] = df['XP'].apply(asignar_nivel)

# Mostrar resultado
print(df.head())
