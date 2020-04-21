import boto3

ec2_client = boto3.client('ec2')
# Client for sending email and text notifications
sns_client = boto3.client('sns')

volumes = ec2_client.describe_volumes()

zone = 'us-east-1d'
unused_vols = []
size = 0
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0 or volume['AvailabilityZone'] == zone:
        print(volume)
        unused_vols.append(volume['VolumeId'])
        size += volume['Size']

email_body = "##### Unused Volumes or Zone is 'us-east-1d'##### \n"

for vol in unused_vols:
    email_body += "VolumeId = {} \n".format(vol)

email_body += "\n\n Total Unused Volume Size ={}".format(size)

# Send Email
sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:813637113719:Volume_EC2_Alerts',
    Subject="Unused Volumes or Region as 'us-east-1'",
    Message=email_body
)
