from django.db import models
from uuid import uuid4


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Data de atualização', auto_now=True)
    is_active = models.BooleanField(verbose_name='Ativo?', default=True)

    class Meta:
        abstract = True
