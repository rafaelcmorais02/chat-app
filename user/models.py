from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from dao.db import Base
from dao.fields import PhoneField, CnpjField
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email=email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email=email), **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser, Base):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(verbose_name='Primeiro nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    phone_number = PhoneField(verbose_name='Número de telefone')
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(verbose_name='Colaborador da equipe?', default=False)
    is_superuser = models.BooleanField(verbose_name='Super usuário?', default=False)
    is_company_admin = models.BooleanField(verbose_name='Admin da empresa?', default=False)
    is_company_staff = models.BooleanField(verbose_name='Colaborador da empresa?', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Company(Base):
    name = models.CharField(verbose_name='Nome da empresa', max_length=50)
    cnpj = CnpjField(verbose_name='CNPJ', unique=True)
    phone_number = PhoneField(verbose_name='Número de telefone', unique=True)
    max_admin_user = models.IntegerField(default=1)
    max_staff_user = models.IntegerField(default=1)


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
