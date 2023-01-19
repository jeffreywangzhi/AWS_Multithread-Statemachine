#HTTP Request Size
#0817FanoutFunction

import json
import requests
import re

def lambda_handler(event, context):
    step = event['iterator']['index']-1

    PATH = event['src'][step]['filePath']

    response = requests.head(PATH)
    
    size = int(response.headers['Content-Length'])
    
    PartialNAME = re.split('\/|\.',PATH)
    fileName = PartialNAME[len(PartialNAME)-2]
    
    PartialPATH = PATH.split('.')
    fileType = PartialPATH[len(PartialPATH)-1]

    return {
        'size': size,
        'fileName': fileName,
        'filePath': PATH,
        'fileType': fileType,
        'src' : event['src'],
        'iterator':event['iterator']
    }