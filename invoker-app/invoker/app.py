import json

import boto3
import requests
import os
import logging
logger = logging.getLogger()
logger.setLevel("DEBUG")

client = boto3.client('lambda')

def lambda_handler(event, context):

    response = client.invoke(FunctionName=os.environ['INVOKEE_FUNCTION_ARN'])
    payload = json.loads(response["Payload"].read())
    logger.debug(json.dumps(payload, ensure_ascii=False, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps(json.loads(payload["body"]), ensure_ascii=False, indent=2),
    }
