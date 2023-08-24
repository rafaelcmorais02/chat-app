from rest_framework.serializers import ModelSerializer
from lead.models import Lead


class LeadCreateSerializer(ModelSerializer):
    class Meta:
        model = Lead
        exclude = ('owner', 'company')


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
