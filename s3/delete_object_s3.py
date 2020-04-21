import boto3

s3_client = boto3.client('s3')

response = s3_client.delete_object(
    Bucket='boto3s3',
    Key='create_bucket.py'
)