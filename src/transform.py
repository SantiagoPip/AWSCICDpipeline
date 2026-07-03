import pandas as pd

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['email'])
    df['email'] = df['email'].str.lower()
    return df