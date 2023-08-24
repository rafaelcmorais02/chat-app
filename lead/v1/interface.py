from lead.v1.lead_status.service import create_lead_status


def create_lead_status_created(lead):
    return create_lead_status(lead=lead, value='created')
