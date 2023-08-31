from dao.serializers import ReadOnlyModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from authentication.models import User


class UserResponseSerializer(ReadOnlyModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class TokenResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class PasswordRedefinitionRequestSerializer(serializers.Serializer):
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


class PasswordRedefinitionResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class GoogleAuthRequestSerializer(serializers.Serializer):
    credential = serializers.CharField()
