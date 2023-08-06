from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from registration.models import Company
from drf_yasg.utils import swagger_auto_schema
from .service import create_company
from authentication.permissions import IsAdmAccount
from rest_framework.permissions import IsAuthenticated


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


@swagger_auto_schema(method='POST', request_body=CompanySerializer, operation_description='Create a Company')
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmAccount])
def create_company_view(request):
    data = request.data
    serializer = CompanySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    company = create_company(**validated_data)
    return Response(data=CompanySerializer(instance=company).data, status=201)
