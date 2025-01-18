import boto3

sqs = boto3.client('sqs', region_name='us-east-1')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/024948959409/sqs-testing'

response = sqs.receive_message(
    QueueUrl=QUEUE_URL,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20,
    VisibilityTimeout=30
)

if 'Messages' in response:
    for message in response['Messages']:
        print(f"Mensagem: {message['Body']}")
        print("Processando mensagem...")
        print("[...]")
        print("Deletando mensagem....")
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )
else:
    print("Sem mensagens na fila.")

