from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from dao.serializers import ReadOnlyModelSerializer
from communication.models import FlowDefinition


class FlowDefinitionResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        fields = '__all__'
        model = FlowDefinition


class CreateFlowDefinitionRequestSerializer(ModelSerializer):
    def validate(self, attrs):
        super().validate(attrs)
        request = self.context
        account = request.user.account
        if account.flow_definitions.filter(trigger=attrs.get('trigger')).filter(is_active=True):
            raise ValidationError({
                'message': 'Is not allowed to have two active flows with the same trigger'
            })
        return attrs

    class Meta:
        exclude = ('owner',)
        model = FlowDefinition
