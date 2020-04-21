import boto3

client = boto3.client('ec2')
# client.start_instances(InstanceIds=['i-0e479666b422824c5'])
# client.stop_instances(InstanceIds=['i-0e479666b422824c5'])
response = client.terminate_instances(InstanceIds=['i-00685c4a5cf3e02d0'], DryRun=False)

for instances in response['TerminatingInstances']:
    print('The instance with {} id terminated'.format(instances['InstanceId']))
