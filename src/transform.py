import pandas as pd

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminamos filas donde el email esté vacío y pasamos a minúsculas
    df = df.dropna(subset=['email'])
    df['email'] = df['email'].str.lower()
    return df