from django.db import models
from dao.fields import PhoneField, CnpjField
from dao.db import Base
from authentication.models import User
from subscription.models import Plan


class Company(Base):
    plan = models.ForeignKey(Plan, verbose_name='Plano', on_delete=models.PROTECT, related_name='companies')
    name = models.CharField(verbose_name='Nome da empresa', max_length=50)
    cnpj = CnpjField(verbose_name='CNPJ', unique=True)
    phone_number = PhoneField(verbose_name='Número de telefone', unique=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-created_at']


class Account(User):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='accounts', null=True, blank=True)
    first_name = models.CharField(verbose_name='Primeiro nome', max_length=50)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=50)
    phone_number = PhoneField(verbose_name='Número de telefone')
    is_company_admin = models.BooleanField(verbose_name='Administrador da empresa?', default=False)
    is_company_staff = models.BooleanField(verbose_name='Colaborador da empresa?', default=True)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
        ordering = ['-created_at']

    def save(self) -> None:
        self.full_name = f'{self.first_name} {self.last_name}'
        return super().save()
