import boto3
import json
from pkg.dto.utente_dto import UtenteDto

class EmailSender:
    def send(self, user: UtenteDto):

        self.sns = boto3.client('sns', endpoint_url='http://localhost:4566', 
                    region_name='us-east-1',
                    aws_access_key_id='test', aws_secret_access_key='test')

        response = self.sns.publish(
            TopicArn='arn:aws:sns:us-east-1:000000000000:email-topic',
            Message=json.dumps({
                'email': user.email,
                'subject': 'Prenotazione Confermata',
                'body': f'Grazie {user.nome} per aver secelto il nostro servizio'
            })
        )
        print(f"Inviato: {response['MessageId']}")
