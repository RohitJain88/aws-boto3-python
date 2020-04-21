import boto3

ec2 = boto3.resource('ec2')

# Client for sending email and text notifications
sns_client = boto3.client('sns')

backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]

snapshot_ids = []
# Looping through list of ec2 Instance
for instance in ec2.instances.filter(Filters=backup_filter):
    for volume in instance.volumes.all():
        snapshot = volume.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

# Send Email
sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:813637113719:Snapshots_EC2',
    Subject='EBS Snapshots',
    Message='\n'.join(map(str, snapshot_ids))
)
