#Download Part10
#multipartDownloadP10

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part10'] == -1):
        return {
            'content10': "part10 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part10']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=10,
                UploadId=event['uploadID'],
        )
        
        return {
            'content10': "part10 succeeded",
            'ETagJ':part['ETag']
        }
