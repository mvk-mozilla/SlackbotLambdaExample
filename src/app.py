import json

def lambda_handler(event, context):
    print("Hi CLoudWatch!")
    print ("I am a handler")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('I got a body for u and it comes from an S3 ZIP!!!\n Plus I\'ve been testing'), #err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
        #'body': json.dumps('Hello from Lambda!')
    }
