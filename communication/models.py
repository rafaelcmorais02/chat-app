from dao.db import Base
from django.db import models
from registration.models import Account
from lead.models import Lead
from enum import Enum
from datetime import datetime


class FlowTriggerType(Enum):
    NOVA_MENSAGEM = 'new_message'
    NOVO_LEAD = 'new_lead'

    @classmethod
    def as_choices(cls):
        return [(key.value, key.name) for key in cls]


class FlowElementType(Enum):
    MENSAGEM = 'message'
    RESPOSTA = 'answer'
    ESCOLHA = 'choice'
    ATRASO = 'delay'

    @classmethod
    def as_list(cls):
        return [key.value for key in cls]

    @classmethod
    def as_choices(cls):
        return [(key.value, key.name) for key in cls]


class FlowDefinition(Base):
    name = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    definition = models.JSONField(verbose_name='Definição')
    owner = models.ForeignKey(Account, verbose_name='Dono da definição', on_delete=models.CASCADE, related_name='flow_definitions')
    trigger = models.CharField(verbose_name='Acionador', max_length=20, choices=FlowTriggerType.as_choices())

    class Meta:
        verbose_name = 'Definição de Fluxo'
        verbose_name_plural = 'Definições de Fluxo'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class FlowExecution(Base):
    flow_definition = models.ForeignKey(FlowDefinition, verbose_name='Definição do fluxo', on_delete=models.CASCADE, related_name='flow_executions')
    lead = models.ForeignKey(Lead, verbose_name='Lead', on_delete=models.CASCADE, related_name='flow_executions')
    owner = models.ForeignKey(Account, verbose_name='Dono da definição', on_delete=models.CASCADE, related_name='flow_executions')
    started_at = models.DateTimeField(verbose_name='Data do inicio da execução', blank=True, null=True)
    finished_at = models.DateTimeField(verbose_name='Data do final da execução', blank=True, null=True)

    class Meta:
        verbose_name = 'Execução de Fluxo'
        verbose_name_plural = 'Execuções de Fluxo'
        ordering = ['-created_at']

    @property
    def start(self):
        self.started_at = datetime.now()
        self.save()

    @property
    def finish(self):
        self.finished_at = datetime.now()
        self.save()

    def __str__(self):
        return self.flow_definition.name


class FlowElement(Base):
    flow_execution = models.ForeignKey(FlowExecution, verbose_name='Execução do fluxo', on_delete=models.CASCADE, related_name='flow_elements')
    name = models.CharField(verbose_name='Nome', choices=FlowElementType.as_choices(), max_length=20)
    index = models.PositiveIntegerField(verbose_name='Posição', default=0)
    task_started = models.BooleanField(verbose_name='Tarefa inciada?', default=False)
    task_finished = models.BooleanField(verbose_name='Tarefa finalizada?', default=False)
    started_at = models.DateTimeField(verbose_name='Data do inicio da execução', blank=True, null=True)
    finished_at = models.DateTimeField(verbose_name='Data do final da execução', blank=True, null=True)

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        ordering = ['-created_at']

    @property
    def start(self):
        self.started_at = datetime.now()
        self.task_started = True
        self.save()

    @property
    def finish(self):
        self.finished_at = datetime.now()
        self.task_finished = True
        self.save()

    def __str__(self):
        return f'{self.name}'


class MessageElement(Base):
    flow_element = models.ForeignKey(FlowElement, verbose_name='Elemento do fluxo', on_delete=models.CASCADE, related_name='messages_element')
    content = models.TextField()

    class Meta:
        verbose_name = 'Elemento Mensagem'
        verbose_name_plural = 'Elementos Mensagem'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)
