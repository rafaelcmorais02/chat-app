from rest_framework.serializers import ModelSerializer
from dao.serializers import ReadOnlyModelSerializer
from communication.models import FlowDefinition


class FlowDefinitionResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        fields = '__all__'
        model = FlowDefinition


class CreateFlowDefinitionRequestSerializer(ModelSerializer):
    class Meta:
        exclude = ('owner',)
        model = FlowDefinition
