import requests
import json
import os
import boto3
from base64 import b64decode

ENCRYPTED = os.environ['SLACK_WEBHOOK']
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext'].decode('utf-8')


slack_web_hook = DECRYPTED


def send_slack(event, context):
    print(str(event))
    text = 'EC2 Instance {} Stopped'.format(event['detail']['instance-id'])
    slack_message = {'text': text}
    response = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return response.text
