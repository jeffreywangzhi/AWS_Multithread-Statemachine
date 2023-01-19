#Download Part5
#multipartDownloadP5

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part5'] == -1):
        return {
            'content5': "part5 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part5']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=5,
                UploadId=event['uploadID'],
        )

        return {
            'content5': "part5 succeeded",
            'ETagE':part['ETag']
        }
