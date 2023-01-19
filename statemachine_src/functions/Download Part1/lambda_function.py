#Download Part1
#multipartDownloadP1

import json
import requests
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    
    if(event['part1'] == -1):
        return {
            'content1': "part1 passed",
            'fileName': event['fileName'],
            'fileType': event['fileType'],
            'scr': event['src'],
            'iterator':event['iterator']
        }
    else:
        
        headers = {"Range": "bytes="+event['part1']}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body=response.content,
                Bucket='uploadfilelocation2',
                Key=event['fileName']+"."+event['fileType'],
                PartNumber=1,
                UploadId=event['uploadID'],
        )

        return {
            'content1': "part1 succeeded",
            'fileName': event['fileName'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'ETagA':part['ETag'],
            'uploadID':event['uploadID']
        }