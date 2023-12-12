import os
import requests
import boto3

client=boto3.client('s3')

def lambda_handler(event, context):
    PART = os.environ['PART']
    PARTNUM = f"part{PART}"
    CONTENTNUM = f"content{PART}"
    TARGET_S3 = os.environ['BUCKET']
    ETAG = os.environ['ETAG']

    if(event[PARTNUM] == -1):
        return {
            CONTENTNUM: f"{PARTNUM} passed",
            'fileName': event['fileName'],
            'fileType': event['fileType'],
            'scr': event['src'],
            'iterator':event['iterator']
        }
    else:
        
        headers = {"Range": "bytes="+event[PARTNUM]}
        response = requests.get(event['filePath'],headers=headers)
        
        part = client.upload_part(
                Body = response.content,
                Bucket = TARGET_S3,
                Key = f"{event['fileName']}.{event['fileType']}", 
                PartNumber = int(PART),
                UploadId = event['uploadID'],
        )

        return {
            CONTENTNUM: f"{PARTNUM} succeeded",
            'fileName': event['fileName'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            ETAG:part['ETag'],
            'uploadID':event['uploadID']
        }