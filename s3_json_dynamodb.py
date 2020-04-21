import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    json_file = event['Records'][0]['s3']['object']['key']

    json_object = s3_client.get_object(Bucket=bucket_name, Key=json_file)
    json_file_reader = json_object['Body'].read()

    json_dict = json.loads(json_file_reader)

    table = dynamodb.Table('employees')
    table.put_item(Item=json_dict)

    return {
        'statusCode': 200,
        'body': json.dumps('End of Lambda function!')
    }