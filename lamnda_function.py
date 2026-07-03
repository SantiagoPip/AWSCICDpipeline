import json
from src.transform import limpiar_datos
# Aquí iría tu lógica de boto3 para leer S3...

def lambda_handler(event, context):
    print("¡Lambda ejecutada por el pipeline de CI/CD!")
    return {
        'statusCode': 200,
        'body': json.dumps('¡Procesamiento exitoso!')
    }