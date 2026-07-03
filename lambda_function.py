import json
import pandas as pd
from src.transform import limpiar_datos

def lambda_handler(event, context):
    try:
        # 1. Recibir los datos simulados que llegan a la Lambda
        datos_entrada = event.get('body', [])
        if not datos_entrada:
            return {
                'statusCode': 200,
                'body': json.dumps('No se recibieron datos para procesar.')
            }
            
        # 2. Convertir a DataFrame y usar tu función de la carpeta src
        df = pd.DataFrame(datos_entrada)
        df_limpio = limpiar_datos(df)
        
        # 3. Retornar el resultado limpio con éxito
        return {
            'statusCode': 200,
            'body': df_limpio.to_dict(orient='records')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error en el pipeline: {str(e)}')
        }