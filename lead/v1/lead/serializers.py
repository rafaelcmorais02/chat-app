from rest_framework.serializers import ModelSerializer
from dao.serializers import ReadOnlyModelSerializer
from lead.models import Lead
from lead.v1.lead_status.serializers import LeadStatusResponseSerializer


class LeadCreateRequestSerializer(ModelSerializer):
    class Meta:
        model = Lead
        exclude = ('owner', 'company')


class LeadResponseSerializer(ReadOnlyModelSerializer):
    status = LeadStatusResponseSerializer(many=True)

    class Meta:
        model = Lead
        fields = '__all__'
