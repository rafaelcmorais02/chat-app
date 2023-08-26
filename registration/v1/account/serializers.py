from registration.models import Account
from dao.serializers import ReadOnlyModelSerializer
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers


class AccountResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'cpf', 'company')


class StaffAccountResponseSerializer(ReadOnlyModelSerializer):
    temporary_password = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'cpf', 'company', 'temporary_password')


class CreateStaffAccountRequestSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = ('password',)


class CreateAdmAccountRequestSerializer(ModelSerializer):
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


class UpdateAccountRequestSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('company',)
