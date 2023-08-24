from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from lead.v1.lead.serializers import LeadCreateSerializer
from lead.v1.lead.service import create_lead
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='POST', request_body=LeadCreateSerializer, operation_description='Create Lead')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_lead_view(request):
    data = request.data
    serializer = LeadCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    owner = request.user.account
    company = owner.company
    if not company:
        raise ValidationError('User must register a company before creating a lead')
    lead = create_lead(owner=owner, company=company, **validated_data)
    return Response(data=lead, status=201)
