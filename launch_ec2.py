import boto3

client = boto3.client('ec2')
response = client.run_instances(ImageId='ami-04b9e92b5572fa0d1',
                                InstanceType='t2.micro',
                                MinCount=1,
                                MaxCount=1)

for instance in response['Instances']:
    print(instance['InstanceId'])
