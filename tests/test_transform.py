import pandas as pd
import numpy as np
from src.transform import limpiar_datos

def test_limpiar_datos():
    datos_prueba = pd.DataFrame({
        'id': [1, 2],
        'email': ['TEST@ANVIL.COM', np.nan]
    })
    resultado = limpiar_datos(datos_prueba)
    assert len(resultado) == 1
    assert resultado['email'].iloc[0] == 'test@anvil.com'