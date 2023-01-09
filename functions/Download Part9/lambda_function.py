#Download Part9
#multipartDownloadP9

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part9'] == -1):
        return {
            'content9': "part9 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part9']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=9,
                UploadId=event['uploadID'],
        )
        
        return {
            'content9': "part9 succeeded",
            'ETagI':part['ETag']
        }
