from rest_framework.serializers import ModelSerializer
from lead.models import LeadStatus


class LeadStatusSerializer(ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = ('id', 'value')
