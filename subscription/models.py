from django.db import models
from dao.db import Base


class Plan(Base):
    name = models.CharField(verbose_name='Nome', max_length=50)
    max_adm_account = models.PositiveIntegerField(verbose_name='Número máximo de adms', null=True, blank=True)
    max_staff_account = models.PositiveIntegerField(verbose_name='Número máximo de colaboradores', null=True, blank=True)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        ordering = ['-created_at']
