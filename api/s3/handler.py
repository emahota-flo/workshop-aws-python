import boto3
import os


def createFile(event, context):
    text = event.get("body").get("text")
    fileName = event.get("body").get("fileName")
    Bucket = os.environ.get('BUCKET_NAME')

    s3 = boto3.client('s3')
    s3Resp = s3.put_object(Bucket=Bucket, Key=fileName, Body=text)

    return s3Resp
