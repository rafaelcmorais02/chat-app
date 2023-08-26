from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .service import create_adm_account, update_account, create_staff_account, get_account, create_password_account_staff
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authentication.permissions import IsAdmAccount
from registration.v1.account.serializers import CreateAdmAccountRequestSerializer, CreateStaffAccountRequestSerializer, UpdateAccountRequestSerializer, StaffAccountResponseSerializer, AccountResponseSerializer


openapi_account_response = openapi.Response('', AccountResponseSerializer)
openapi_staff_account_response = openapi.Response('', StaffAccountResponseSerializer)


@swagger_auto_schema(method='POST', request_body=CreateAdmAccountRequestSerializer, operation_description='Create an ADM Account', responses={201: openapi_account_response})
@api_view(['POST'])
def create_adm_account_view(request):
    data = request.data
    serializer = CreateAdmAccountRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = create_adm_account(**validated_data)
    return Response(data=account, status=201)


@swagger_auto_schema(method='POST', request_body=CreateStaffAccountRequestSerializer, operation_description='Create an Staff Account', responses={201: openapi_staff_account_response})
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmAccount])
def create_staff_account_view(request):
    data = request.data
    adm_account = request.user.account
    if not adm_account.company:
        raise ValidationError({
            'message': 'Account must be associated with a company before creating an user'
        })
    serializer = CreateStaffAccountRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    company = adm_account.company
    password = create_password_account_staff(company_cnpj=company.cnpj, account_cpf=validated_data.get('cpf'))
    account = create_staff_account(company=company, password=password, **validated_data)
    return Response(account, status=201)


@swagger_auto_schema(method='PUT', request_body=UpdateAccountRequestSerializer, operation_description='Update an Account with a Company', responses={201: openapi_account_response})
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_account_view(request, pk):
    data = request.data
    serializer = UpdateAccountRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    account = update_account(pk=pk, **validated_data)
    return Response(data=account, status=201)


@swagger_auto_schema(method='GET', operation_description='Get account by id', responses={200: openapi_account_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_account_view(request, pk):
    account = get_account(pk=pk, user=request.user)
    return Response(data=account, status=200)
