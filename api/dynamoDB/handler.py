import boto3
import os


def createItem(event, context):
    fileName = event.get("body").get("fileName")
    TableName = os.environ.get('FILE_LIST_TABLE')

    dynamoDB = boto3.client('dynamodb')
    tableResp = dynamoDB.put_item(
        TableName=TableName,
        Item={
            'id': {
                'S': fileName,
            }
        }
    )
    return tableResp


def getItems(event, context):
    TableName = os.environ.get('FILE_LIST_TABLE')
    dynamoDB = boto3.client('dynamodb')
    tableData = dynamoDB.scan(
        TableName=TableName,
    )
    return tableData
