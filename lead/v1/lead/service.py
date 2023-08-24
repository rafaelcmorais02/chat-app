from lead.models import Lead
from lead.v1.lead.serializers import LeadSerializer
from lead.v1.interface import create_lead_status_created


def create_lead(owner, company, **validated_data):
    lead = Lead(**validated_data)
    lead.owner = owner
    lead.company = company
    lead.save()
    lead_status = create_lead_status_created(lead=lead)
    return {
        "lead": LeadSerializer(instance=lead).data,
        "status": lead_status
    }
