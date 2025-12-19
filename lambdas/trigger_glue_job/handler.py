import boto3
import os

glue = boto3.client("glue")

JOB_NAME = os.environ["JOB_NAME"]

def lambda_handler(event, context):
    response = glue.start_job_run(
        JobName=JOB_NAME
    )
    return {
        "status": "job_started",
        "job": JOB_NAME
    }
