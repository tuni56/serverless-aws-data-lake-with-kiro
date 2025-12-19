import boto3
import os

glue = boto3.client("glue")

CRAWLER_NAME = os.environ["CRAWLER_NAME"]

def lambda_handler(event, context):
    response = glue.start_crawler(
        Name=CRAWLER_NAME
    )
    return {
        "status": "crawler_started",
        "crawler": CRAWLER_NAME
    }
