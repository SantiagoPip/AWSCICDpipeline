import pandas as pd
import numpy as np
from src.transform import limpiar_datos

def test_limpiar_datos():
    # Creamos datos ficticios de prueba, uno viene con email nulo
    datos_prueba = pd.DataFrame({
        'id': [1, 2],
        'email': ['TEST@ANVIL.COM', np.nan]
    })
    
    resultado = limpiar_datos(datos_prueba)
    
    # Verificaciones (Asserts)
    assert len(resultado) == 1  # Debería quedar solo 1 fila (se elimina el nulo)
    assert resultado['email'].iloc[0] == 'test@anvil.com'  # Debe estar en minúsculas