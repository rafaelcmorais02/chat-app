from dao.db import Base
from django.db import models
from registration.models import Account


class FlowDefinition(Base):
    TRIGGERS = (
        ('new_message', 'nova mensagem'),
        ('new_lead', 'novo lead'),
    )
    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    definition = models.JSONField(verbose_name='Definição')
    owner = models.ForeignKey(Account, verbose_name='Dono da definição', on_delete=models.CASCADE, related_name='flow_definitions')
    trigger = models.CharField(verbose_name='Acionador', max_length=20, choices=TRIGGERS)

    class Meta:
        verbose_name = 'Definição de Fluxo'
        verbose_name_plural = 'Definições de Fluxo'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
