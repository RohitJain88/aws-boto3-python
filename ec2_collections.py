import boto3

ec2 = boto3.resource('ec2')
'''
To fetch all the instances for the account
'''
# for instance in ec2.instances.all():

'''
To fetch all the instances with the specified filter
'''
# for instance in ec2.instances.filter(Filters=[
#         {
#             'Name': 'availability-zone',
#             'Values': ['us-east-1d']
#         }
# ]):
#     print('Instance Id is {} and Instance type is {}'.format(instance.instance_id, instance.instance_type))

'''
To fetch all running instances and stop them
'''
ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
]).stop()