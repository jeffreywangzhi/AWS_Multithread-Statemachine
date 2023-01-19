#Download Part6
#multipartDownloadP6

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part6'] == -1):
        return {
            'content6': "part6 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part6']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=6,
                UploadId=event['uploadID'],
        )
        
        return {
            'content6': "part6 succeeded",
            'ETagF':part['ETag']
        }
