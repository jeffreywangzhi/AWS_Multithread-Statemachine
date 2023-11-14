#Divide into parts
#0817UploadS3

import json
import base64
import requests

import boto3
client=boto3.client('s3')

def split_integer(m, n):
    assert n > 0
    quotient = int(m / n)
    remainder = m % n
    if remainder > 0:
        return [quotient] * (n - remainder) + [quotient + 1] * remainder
    if remainder < 0:
        return [quotient - 1] * -remainder + [quotient] * (n + remainder)
    return [quotient] * n

def lambda_handler(event, context):
    
    response = client.create_multipart_upload(Bucket = 'uploadfilelocation2', Key = event['fileName']+"."+event['fileType'])
    
    if(event['size']<=0):
        
        return {
            'part1': -1,
            'part2': -1,
            'part3': -1,
            'part4': -1,
            'part5': -1,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
    
    if(event['size']/10>=5242880):
        
        divList = split_integer(event['size'],10)
        d1 = "0-"+str(divList[0])
        d2 = str(divList[0]+1)+"-"+str(divList[0]+divList[1])
        d3 = str(divList[0]+divList[1]+1)+"-"+str(divList[0]+divList[1]+divList[2])
        d4 = str(divList[0]+divList[1]+divList[2]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3])
        d5 = str(divList[0]+divList[1]+divList[2]+divList[3]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4])
        d6 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5])
        d7 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6])
        d8 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7])
        d9 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+divList[8])
        d10 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+divList[8]+1)+"-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': d7,
            'part8': d8,
            'part9': d9,
            'part10': d10,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/9>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-26214400"
        d6 = "26214401-31457280"
        d7 = "31457281-36700160"
        d8 = "36700161-41943040"
        d9 = "41943041-47185920"
        d10 = "47185921-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': d7,
            'part8': d8,
            'part9': d9,
            'part10': d10,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/8>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-26214400"
        d6 = "26214401-31457280"
        d7 = "31457281-36700160"
        d8 = "36700161-41943040"
        d9 = "41943041-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': d7,
            'part8': d8,
            'part9': d9,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/7>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-26214400"
        d6 = "26214401-31457280"
        d7 = "31457281-36700160"
        d8 = "36700161-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': d7,
            'part8': d8,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/6>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-26214400"
        d6 = "26214401-31457280"
        d7 = "31457281-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': d7,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/5>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-26214400"
        d6 = "26214401-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': d6,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/4>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-20971520"
        d5 = "20971521-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': d5,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/3>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-15728640"
        d4 = "15728641-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': d4,
            'part5': -1,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/2>=5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-10485760"
        d3 = "10485761-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': d3,
            'part4': -1,
            'part5': -1,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
        
    elif(event['size']/1>5242880):
        
        d1 = "0-5242880"
        d2 = "5242881-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': d2,
            'part3': -1,
            'part4': -1,
            'part5': -1,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }    
        
    else:

        d1 = "0-"+str(event['size'])
        
        return {
            'part1': d1,
            'part2': -1,
            'part3': -1,
            'part4': -1,
            'part5': -1,
            'part6': -1,
            'part7': -1,
            'part8': -1,
            'part9': -1,
            'part10': -1,
            'fileName': event['fileName'],
            'filePath': event['filePath'],
            'fileType': event['fileType'],
            'src': event['src'],
            'iterator':event['iterator'],
            'uploadID':response['UploadId']
        }
    
    # if(event['size']<=52428800):
    #     return {
    #         'part1': "0-"+str(event['size']),
    #         'part2': -1,
    #         'part3': -1,
    #         'part4': -1,
    #         'part5': -1,
    #         'part6': -1,
    #         'part7': -1,
    #         'part8': -1,
    #         'part9': -1,
    #         'part10': -1,
    #         'fileName': event['fileName'],
    #         'filePath': event['filePath'],
    #         'fileType': event['fileType'],
    #         'src': event['src'],
    #         'iterator':event['iterator'],
    #         'uploadID':response['UploadId']
    #     }
        
        
        
    # else:
        
    #     divList = split_integer(event['size'],10)
    #     d1 = "0-"+str(divList[0])
    #     d2 = str(divList[0]+1)+"-"+str(divList[0]+divList[1])
    #     d3 = str(divList[0]+divList[1]+1)+"-"+str(divList[0]+divList[1]+divList[2])
    #     d4 = str(divList[0]+divList[1]+divList[2]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3])
    #     d5 = str(divList[0]+divList[1]+divList[2]+divList[3]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4])
    #     d6 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5])
    #     d7 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6])
    #     d8 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7])
    #     d9 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+1)+"-"+str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+divList[8])
    #     d10 = str(divList[0]+divList[1]+divList[2]+divList[3]+divList[4]+divList[5]+divList[6]+divList[7]+divList[8]+1)+"-"+str(event['size'])
    
    #     return {
    #         'part1': d1,
    #         'part2': d2,
    #         'part3': d3,
    #         'part4': d4,
    #         'part5': d5,
    #         'part6': d6,
    #         'part7': d7,
    #         'part8': d8,
    #         'part9': d9,
    #         'part10': d10,
    #         'fileName': event['fileName'],
    #         'filePath': event['filePath'],
    #         'fileType': event['fileType'],
    #         'src': event['src'],
    #         'iterator':event['iterator'],
    #         'uploadID':response['UploadId']
    #     }
