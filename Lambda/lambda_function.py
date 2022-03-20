import json

def lambda_handler(event, context):
    if 'queryStringParameters' in event:
        print(event['queryStringParameters']['first_name'])
        print(event['queryStringParameters']['last_name'])
        body = 'Hello {} {}!'.format(
            event['queryStringParameters']['first_name'],
            event['queryStringParameters']['last_name'])  
    else:
        print('No parameters!')
        body = 'Who are you?'
        
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
