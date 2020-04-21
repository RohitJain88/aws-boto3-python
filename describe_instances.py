import boto3

client = boto3.client('ec2')
response = client.describe_instances(Filters=[{
    'Name': 'tag:Env',
    'Values': ['Stage-1']
}])

for reservation in response['Reservations']:
    for instances in reservation['Instances']:
        print("The Instance Id is {}".format(instances['InstanceId']))
        print("The Instance {} has AvailabilityZone as  {}".format(instances['InstanceId'],
                                                                   instances['Placement']['AvailabilityZone']))