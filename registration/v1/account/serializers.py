from registration.models import Account
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = ('password', )


class AdmAccountCreateSerializer(ModelSerializer):
    password_validation = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, attrs):
        if (attrs.get('password') != attrs.get('password_validation')):
            raise ValidationError({
                'message': 'the passwords must match'
            })
        attrs.pop('password_validation')
        return super().validate(attrs)


class AccountUpdateSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('company',)
