import boto3
import json

#comprehend = boto3.client (service_name='comprehend', region_name='eu-west-1')

comprehend = boto3.client(
    'comprehend',
    aws_access_key_id='AKIAJQ2GE4BPYJHQJMSA',
    aws_secret_access_key='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',
    region_name='eu-west-1'
)


text = "Donde estan mis maletas, no se ni como ir a buscarlo"
text1 = ["Where I can find my luggage"]

print('Calling DetectKeyPhrases')
print(json.dumps (comprehend.batch_detect_key_phrases(TextList=text1, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')