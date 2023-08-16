from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from registration.models import Account
from .service import create_adm_account, update_account, create_staff_account, get_account
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authentication.permissions import IsAdmAccount


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


get_account_response = openapi.Response('', AccountSerializer)


@swagger_auto_schema(method='POST', request_body=AdmAccountCreateSerializer, operation_description='Create an ADM Account')
@api_view(['POST'])
def create_adm_account_view(request):
    data = request.data
    serializer = AdmAccountCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = create_adm_account(**validated_data)
    return Response(data=AccountSerializer(instance=account).data, status=201)


@swagger_auto_schema(method='POST', request_body=AccountSerializer, operation_description='Create an Staff Account')
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmAccount])
def create_staff_account_view(request):
    data = request.data
    adm_account = request.user.account
    if not hasattr(adm_account, 'company'):
        raise ValidationError('User must register a company before creating an user')
    serializer = AccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account, password = create_staff_account(company=adm_account.company, **validated_data)
    response = {
        'account': AccountSerializer(instance=account).data,
        'password': password
    }
    return Response(data=response, status=201)


@swagger_auto_schema(method='PUT', request_body=AccountUpdateSerializer, operation_description='Update an Account with a Company')
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_account_view(request, pk):
    data = request.data
    serializer = AccountUpdateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = update_account(pk=pk, **validated_data)
    return Response(data=AccountSerializer(instance=account).data, status=201)


@swagger_auto_schema(method='GET', operation_description='Get account by id', responses={200: get_account_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_account_view(request, pk):
    account = get_account(pk=pk, user=request.user)
    return Response(data=AccountSerializer(instance=account).data, status=200)
