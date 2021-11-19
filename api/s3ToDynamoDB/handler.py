import boto3
import os


def s3ToDynamoDB(event, context):
    Records = event.get('Records')
    fileName = Records[0].get('s3').get('object').get('key')
    TableName = os.environ.get('FILE_LIST_TABLE')
    dynamoDB = boto3.client('dynamodb')
    dynamoDB.put_item(
        TableName=TableName,
        Item={
            'id': {
                'S': fileName,
            }
        }
    )
