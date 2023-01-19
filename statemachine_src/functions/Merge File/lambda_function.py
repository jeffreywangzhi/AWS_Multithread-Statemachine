#Merge File
#multipartMerge

import json
import requests
import boto3
client=boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):

    fileName = event[0]['fileName']+'.'+event[0]['fileType']
    
    part_info = {
        'Parts':[]
    }
    if('ETagA' in event[0]):
        part_info['Parts'].append({
            'PartNumber':1,
            'ETag':event[0]['ETagA']
        })
    if('ETagB' in event[1]):
        part_info['Parts'].append({
            'PartNumber':2,
            'ETag':event[1]['ETagB']
        })
    if('ETagC' in event[2]):
        part_info['Parts'].append({
            'PartNumber':3,
            'ETag':event[2]['ETagC']
        })
    if('ETagD' in event[3]):
        part_info['Parts'].append({
            'PartNumber':4,
            'ETag':event[3]['ETagD']
        })
    if('ETagE' in event[4]):
        part_info['Parts'].append({
            'PartNumber':5,
            'ETag':event[4]['ETagE']
        })
    if('ETagF' in event[5]):
        part_info['Parts'].append({
            'PartNumber':6,
            'ETag':event[5]['ETagF']
        })
    if('ETagG' in event[6]):
        part_info['Parts'].append({
            'PartNumber':7,
            'ETag':event[6]['ETagG']
        })
    if('ETagH' in event[7]):
        part_info['Parts'].append({
            'PartNumber':8,
            'ETag':event[7]['ETagH']
        })
    if('ETagI' in event[8]):
        part_info['Parts'].append({
            'PartNumber':9,
            'ETag':event[8]['ETagI']
        })
    if('ETagJ' in event[9]):
        part_info['Parts'].append({
            'PartNumber':10,
            'ETag':event[9]['ETagJ']
        })
    
    complete = client.complete_multipart_upload(Bucket='uploadfilelocation2',
                                                Key=fileName,
                                                UploadId=event[0]['uploadID'],
                                                MultipartUpload=part_info)
    
    return {
        'res':'succeeded',
        'src': event[0]['src'],
        'iterator':event[0]['iterator']
    }