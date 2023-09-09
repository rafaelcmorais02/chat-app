import json
from rest_framework.exceptions import ValidationError
from communication.models import FlowDefinition
from communication.v1.flow_definition.serializers import FlowDefinitionResponseSerializer
from communication.models import FlowElementType


def validate_definition(raw_definition):
    ELEMENT_TYPES = FlowElementType.as_list()
    definition = json.loads(raw_definition)
    elements = definition.get('definition').get('elements')
    if not isinstance(elements, list):
        raise ValidationError({
            'message': 'Elements must be a list'
        })
    for element in elements:
        if not element.get('type') in ELEMENT_TYPES:
            raise ValidationError({
                'message': 'Element Type was not identified'
            })
        if element.get('type') == FlowElementType.MENSAGEM.value:
            params = element.get('params')
            if not params:
                raise ValidationError({
                    'message': 'Missing params'
                })
            if not isinstance(params.get('value'), str):
                raise ValidationError({
                    'message': 'Value must be a string'
                })
        else:
            raise ValidationError({
                'message': f'Element type does not match any of the expected values: {ELEMENT_TYPES}'
            })
    return True


def create_definition(request, **validated_data):
    flow_definition = FlowDefinition(**validated_data)
    flow_definition.owner = request.user.account
    flow_definition.save()
    return FlowDefinitionResponseSerializer(instance=flow_definition).data
