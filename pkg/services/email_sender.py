import boto3
import json

class EmailSender:
    def send(self):

        self.sns = boto3.client('sns', endpoint_url='http://localhost:4566', 
                    region_name='us-east-1',
                    aws_access_key_id='test', aws_secret_access_key='test')

        response = self.sns.publish(
            TopicArn='arn:aws:sns:us-east-1:000000000000:email-topic',
            Message=json.dumps({
                'email': 'test@example.com',
                'subject': 'Prenotazione Confermata',
                'body': 'Grazie per aver secelto il nostro servizio'
            })
        )

        print(f"Inviato: {response['MessageId']}")
