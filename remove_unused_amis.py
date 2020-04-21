import boto3

ec2_client = boto3.client('ec2')
instances = ec2_client.describe_instances()

used_amis = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

print(used_amis)

unique_amids = set(used_amis)
print(unique_amids)

# get custom amis from the account
custom_images = ec2_client.describe_images(
    Filters=[
            {
                'Name': 'state',
                'Values': [
                    'available',
                ]
            },
        ],
    Owners=['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

# Delete unused AMIs
for custom_ami in custom_amis_list:
    if custom_ami not in unique_amids:
        print("Deregistering ami {}".format(custom_ami))
        ec2_client.deregister_image(ImageId=custom_ami)

