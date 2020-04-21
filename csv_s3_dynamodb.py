import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee_csv')


def lambda_handler(event, context):
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_filename = event['Records'][0]['s3']['object']['key']

    resp = s3_client.get_object(Bucket=bucket_name, Key=s3_filename)

    data = resp['Body'].read().decode("utf-8")
    employees = data.split("\n")

    for emp in employees:
        print(emp)
        data = emp.split(",")
        # Add data to dynamodb
        try:
            table.put_item(
                Item={
                    "id": data[0],
                    "name": data[1],
                    "location": data[2]
                })
        except Exception as e:
            print("End of file")
