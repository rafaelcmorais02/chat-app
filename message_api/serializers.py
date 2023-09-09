from rest_framework import serializers


class TextMessageSerializer(serializers.Serializer):

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.fields['body'] = serializers.CharField(initial=message)
        self.fields['preview_url'] = serializers.BooleanField(initial=False)


class MessageSerializer(serializers.Serializer):
    def __init__(self, phone_number, text, **kwargs):
        super().__init__(**kwargs)
        self.fields['messaging_product'] = serializers.CharField(initial='whatsapp')
        self.fields['recipient_type'] = serializers.CharField(initial='individual')
        self.fields['to'] = serializers.CharField(initial=phone_number)
        self.fields['type'] = serializers.CharField(initial='text')
        self.fields['text'] = text
