from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from communication.v1.flow_definition.serializers import CreateFlowDefinitionRequestSerializer, FlowDefinitionResponseSerializer
from communication.v1.flow_definition.service import create_definition, validate_definition


openapi_flow_definition_response = openapi.Response('', FlowDefinitionResponseSerializer)


@swagger_auto_schema(method='POST', request_body=CreateFlowDefinitionRequestSerializer, operation_description='Create an ADM Account', responses={201: openapi_flow_definition_response})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_definition_view(request):
    data = request.data
    serializer = CreateFlowDefinitionRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    validate_definition(validated_data.get('definition'))
    definition = create_definition(request=request, **validated_data)
    return Response(data=definition, status=201)
