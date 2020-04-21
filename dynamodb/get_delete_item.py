import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

# GET Item
resp = table.get_item(
    Key={
        'emp_id': 1
    },
    AttributesToGet=['Salary']
)

print(resp['Item'])

# DELETE Item
table.delete_item(
    Key={
        'emp_id': 1
    }
)