import boto3
import psycopg2
import os
from pprint import pprint
import warnings

warnings.filterwarnings('ignore', category=FutureWarning, module='botocore.client')

con = psycopg2.connect(host='localhost', database='10i9', user='10i9', password='')


sqs_client =boto3.client("sqs", region_name="us-east-2",
    aws_access_key_id=os.environ.get('AKIAWVMM5Q4JX4YSDAWJ'),
                   aws_secret_access_key=os.environ.get('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'))
def getMessage():
    try:
        queue = sqs_client.get_queue_url(QueueName='teste-1.fifo')
        response = sqs_client.receive_message(
        QueueUrl=queue['QueueUrl'],
        AttributeNames=[
        'SentTimestamp'
     ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
        'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=10
        )

        message = response['Messages']

        for msg in message:
            body = msg['Body']
            print(body)

            cur = con.cursor()
            cur.execute(body)

            con.commit()
            
    except Exception as e:
        pprint("Error in recieving message \n{}".format(e))
        return None
if __name__ == "__main__":
    getMessage()