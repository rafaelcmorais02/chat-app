from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from lead.models import Lead, LeadStatus
from communication.controller import Controller
from dao.serializers import ReadOnlyModelSerializer

controller = Controller()


class LeadStatusEventSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = LeadStatus
        fields = ('id', 'value', 'created_at')


class LeadEventSerializer(ReadOnlyModelSerializer):
    status = LeadStatusEventSerializer(many=True)

    class Meta:
        model = Lead
        fields = '__all__'


@receiver(post_save, sender=Lead)
def handle_event(sender, instance, created, *args, **kwargs):
    lead = LeadEventSerializer(instance=instance).data
    event_data = {
        'event': 'lead_created' if created else 'lead_updated',
        'record': lead,
        'timestamp': datetime.now().isoformat()
    }
    controller.communication_event(event_data)
