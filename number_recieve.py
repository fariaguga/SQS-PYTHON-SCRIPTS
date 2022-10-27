import boto3
import json

def receive_message():
    sqs_client = boto3.client("sqs", region_name="us-west-2")
    response = sqs_client.receive_message(
        QueueUrl="https://us-west-2.queue.amazonaws.com/xxx/my-new-queue",
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")