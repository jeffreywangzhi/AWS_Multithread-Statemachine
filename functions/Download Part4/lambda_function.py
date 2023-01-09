#Download Part4
#multipartDownloadP4

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part4'] == -1):
        return {
            'content4': "part4 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part4']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=4,
                UploadId=event['uploadID'],
        )
        
        return {
            'content4': "part4 succeeded",
            'ETagD':part['ETag']
        }
