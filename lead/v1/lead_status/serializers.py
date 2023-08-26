from dao.serializers import ReadOnlyModelSerializer
from lead.models import LeadStatus


class LeadStatusResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = LeadStatus
        fields = ('id', 'value', 'created_at')
