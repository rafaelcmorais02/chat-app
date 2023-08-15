from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from registration.models import Account
from .service import create_adm_account, update_account
from drf_yasg.utils import swagger_auto_schema


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


class AdmAccountUpdateSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('company',)


@swagger_auto_schema(method='POST', request_body=AdmAccountCreateSerializer, operation_description='Create an ADM Account')
@api_view(['POST'])
def create_adm_account_view(request):
    data = request.data
    serializer = AdmAccountCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = create_adm_account(**validated_data)
    return Response(data=AdmAccountCreateSerializer(instance=account).data, status=201)


@swagger_auto_schema(method='PUT', request_body=AdmAccountUpdateSerializer, operation_description='Update an Account with a Company')
@api_view(['PUT'])
def update_account_view(request, pk):
    data = request.data
    serializer = AdmAccountUpdateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = update_account(pk=pk, **validated_data)
    return Response(data=AdmAccountCreateSerializer(instance=account).data, status=201)
