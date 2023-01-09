#Download Part7
#multipartDownloadP7

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part7'] == -1):
        return {
            'content7': "part7 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part7']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=7,
                UploadId=event['uploadID'],
        )
        
        return {
            'content7': "part7 succeeded",
            'ETagG':part['ETag']
        }
