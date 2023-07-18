# all the following deps are referenced directly from the python sdk
import json
from typing import Dict
from Message import Message


def lambda_handler(event, context):
    headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json"
    }

    try:
        #attempt to parse the json into Message
        message = json.loads(event["body"], object_hook=lambda d: Message(**d))
    except json.JSONDecodeError as e:
        return {
            "body": json.dumps({str(e)}),
            "headers": headers,
            "statusCode": 400
        }

    # convert the message object back into a json
    json_object = {
        "subject": message.get_subject(),
        "body": message.get_body(),
        "email": message.get_email()
    }

    # and return it
    return {
        "body": json.dumps(json_object),
        "headers": headers,
        "statusCode": 200
    }


if __name__ == "__main__":
    # It's a temp code for testing purposes.
    event_ = {}
    print(lambda_handler(event_, None))
