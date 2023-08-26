from rest_framework.exceptions import ValidationError
from lead.models import Lead
from lead.v1.lead.serializers import LeadResponseSerializer
from lead.v1.interface import create_lead_status_created


def create_lead(owner, company, **validated_data):
    if not company:
        raise ValidationError({
            'message': 'Account must be associated with a company before creating an user'
        })
    lead = Lead(**validated_data)
    lead.owner = owner
    lead.company = company
    lead.save()
    create_lead_status_created(lead=lead)
    return LeadResponseSerializer(instance=lead).data
