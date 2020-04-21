import boto3

s3_client = boto3.client('s3')

response = s3_client.select_object_content(
    Bucket='boto3s3',
    Key='files/employee.csv',
    Expression='Select s.Name, s.Location from S3Object s',
    ExpressionType='SQL',
    InputSerialization={
        'CSV': {
            'FileHeaderInfo': 'USE',
        }
    },
    OutputSerialization={
        'JSON': {}
    }
)

# Loop through payload object
for event in response['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode())

