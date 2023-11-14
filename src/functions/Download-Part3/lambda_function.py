#Download Part3
#multipartDownloadP3

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part3'] == -1):
        return {
            'content3': "part3 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part3']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=3,
                UploadId=event['uploadID'],
        )
        
        return {
            'content3': "part3 succeeded",
            'ETagC':part['ETag']
        }
