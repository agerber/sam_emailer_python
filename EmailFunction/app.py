# all the following deps are referenced directly from the python sdk
import json
from typing import Dict
from message import Message


def lambda_handler(event, context):

    #headers we use to send back data to the caller
    headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json"
    }

    try:
        # the body of the event contains the message as a json object, which we can decompose using a dictionary
        dict = json.loads(event["body"])

        subject = dict["subject"]
        email_body = dict["email_body"]
        email = dict["email"]
        message = Message(subject=subject, email_body=email_body, email=email)

    except json.JSONDecodeError as e:
        return {
            "body": json.dumps({str(e)}),
            "headers": headers,
            "statusCode": 400
        }


    # convert the message object back into a json
    json_object = {
        "subject": message.subject,
        "email_body": message.email_body,
        "email": message.email
    }


    # and return it
    return {
        "body": json.dumps(json_object),
        "headers": headers,
        "statusCode": 201
    }

