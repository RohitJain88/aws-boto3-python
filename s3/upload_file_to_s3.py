import boto3

s3_client = boto3.client('s3')

file_reader = open('create_bucket.py').read()
print(file_reader)
response = s3_client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='boto3s3',
    Key='create_bucket.py'
)