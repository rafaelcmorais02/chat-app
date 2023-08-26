from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .service import create_company
from authentication.permissions import IsAdmAccount
from registration.v1.company.serializers import CreateCompanyRequestSerializer, CompanyResponseSerializer


openapi_account_response = openapi.Response('', CompanyResponseSerializer)


@swagger_auto_schema(method='POST', request_body=CreateCompanyRequestSerializer, operation_description='Create a Company', responses={201: openapi_account_response})
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmAccount])
def create_company_view(request):
    data = request.data
    serializer = CreateCompanyRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    company = create_company(request=request, **validated_data)
    return Response(data=company, status=201)
