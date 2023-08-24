from django.db import models
from dao.fields import PhoneField, CpfField
from dao.db import Base
from registration.models import Account, Company


class Lead(Base):
    owner = models.ForeignKey(Account, verbose_name='Dono do lead', on_delete=models.PROTECT, related_name='leads')
    company = models.ForeignKey(Company, verbose_name='Empresa', on_delete=models.PROTECT, related_name='leads')
    first_name = models.CharField(verbose_name='Primeiro nome', max_length=50)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=50)
    cpf = CpfField(verbose_name='CPF', null=True, blank=True)
    phone_number = PhoneField(verbose_name='Número de telefone', unique=True)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LeadStatus(Base):
    LEAD_STATUS = (
        ('created', 'criado'),
        ('on_touch', 'em contato'),
        ('verified', 'verificado'),
        ('not_verified', 'não verificado')
    )

    lead = models.ForeignKey(Lead, verbose_name='Lead', on_delete=models.CASCADE, related_name='status')
    value = models.CharField(verbose_name='Status', max_length=50, choices=LEAD_STATUS, default='created')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['-created_at']

    def __str__(self):
        return self.value
