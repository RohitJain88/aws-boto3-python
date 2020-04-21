import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.put_item(
    Item={
        'emp_id': 1,
        'Name': 'Rohit',
        'Salary': 'USD 150000'
    }
)