from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class PasswordSerializer(serializers.Serializer):
    username = serializers.EmailField()
    old_password = serializers.CharField()
    password = serializers.CharField()
    password_validation = serializers.CharField()

    def validate(self, attrs):
        if (attrs.get('password') != attrs.get('password_validation')):
            raise serializers.ValidationError({
                'message': 'the passwords must match'
            })
        attrs.pop('password_validation')
        return super().validate(attrs)