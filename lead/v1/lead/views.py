from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from lead.v1.lead.serializers import LeadCreateRequestSerializer, LeadResponseSerializer
from lead.v1.lead.service import create_lead
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


openapi_lead_response = openapi.Response('', LeadResponseSerializer)


@swagger_auto_schema(method='POST', request_body=LeadCreateRequestSerializer, operation_description='Create Lead', responses={201: openapi_lead_response})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_lead_view(request):
    data = request.data
    serializer = LeadCreateRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    owner = request.user.account
    company = owner.company
    lead = create_lead(owner=owner, company=company, **validated_data)
    return Response(data=lead, status=201)
