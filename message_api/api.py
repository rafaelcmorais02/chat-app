from django.conf import settings
import json
from httpx import Client
from message_api.serializers import MessageSerializer, TextMessageSerializer


class Whatsapp:
    __url = settings.WHATSAPP_URL
    __headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.WHATSAPP_TOKEN}'
    }

    def __init__(self, timeout=150):
        self.__http = Client(timeout=timeout)

    def send_message(self, phone_number, message):
        data = self.__create_message_payload(phone_number=phone_number, message=message)
        raw_reponse = self.__http.post(self.__url, data=json.dumps(data), headers=self.__headers)
        return raw_reponse.json()

    def __create_message_payload(self, phone_number, message):
        text_serializer = TextMessageSerializer(message=message)
        message_serializer = MessageSerializer(phone_number=phone_number, text=text_serializer)
        return message_serializer.data
