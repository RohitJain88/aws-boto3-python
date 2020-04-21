import boto3

s3_client = boto3.client('s3')

response = s3_client.list_objects(
    Bucket='boto3s3',
)

for content in response['Contents']:
    print('Keys present : {}'.format(content['Key']))