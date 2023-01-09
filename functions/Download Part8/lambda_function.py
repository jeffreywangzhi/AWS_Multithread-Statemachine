#Download Part8
#multipartDownloadP8

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part8'] == -1):
        return {
            'content8': "part8 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part8']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=8,
                UploadId=event['uploadID'],
        )
        
        return {
            'content8': "part8 succeeded",
            'ETagH':part['ETag']
        }
