#Iterator
#IteratorFunction

import json

def lambda_handler(event, context):
    
    return {
        'src': event['src'],
        'count':len(event['src'])+1,
        'index':0,
        'step':1
    }