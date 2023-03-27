import pandas as pd
import boto3
from datetime import datetime, timedelta


# Especificar el bucket y la ruta de la carpeta a eliminar
s3= boto3.resource("s3")
bucket_name = ''
bucket = s3.Bucket(bucket_name)
days_ago = datetime.now() - timedelta(days=)

eliminados=[]
for obj in bucket.objects.all():
    try:
        if obj.last_modified.replace(tzinfo=None) < days_ago:
            obj.delete()
            eliminados.append(obj)
    except:
        print('no data')
        
#cant eliminada
print(len(eliminados))
print(eliminados)
