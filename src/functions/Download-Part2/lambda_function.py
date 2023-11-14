#Download Part2
#multipartDownloadP2

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part2'] == -1):
        return {
            'content2': "part2 passed"
        }
    else:
        
        headers = {"Range": "bytes="+event['part2']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=2,
                UploadId=event['uploadID'],
        )
        
        return {
            'content2': "part2 succeeded",
            'ETagB':part['ETag']
        }
