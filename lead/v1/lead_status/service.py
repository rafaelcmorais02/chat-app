from lead.models import LeadStatus
from lead.v1.lead_status.serializers import LeadStatusResponseSerializer


def create_lead_status(lead, value):
    lead_status = LeadStatus(lead=lead, value=value)
    lead_status.save()
    return LeadStatusResponseSerializer(instance=lead_status).data
