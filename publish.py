import boto3, json

sqs = boto3.client('sqs', region_name='us-east-1')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/024948959409/sqs-testing'

MESSAGE = {
    "Teste": "Mensagem Exemplo"
}

def publish_message(queue_url, message_body, message_attributes={}):
    try:
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(MESSAGE),
            MessageAttributes=message_attributes
        )
        print(f"Sucesso! ID: {response['MessageId']}")
    except Exception as e:
        print(f"Erro: {str(e)}")

publish_message(QUEUE_URL, MESSAGE)