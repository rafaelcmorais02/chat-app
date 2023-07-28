from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from dao.db import Base
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
    full_name = models.CharField('Nome completo', max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    password_redefinition = models.BooleanField(verbose_name='Redefinição de senha', default=False)
    is_staff = models.BooleanField(verbose_name='Colaborador da equipe?', default=False)
    is_superuser = models.BooleanField(verbose_name='Super usuário?', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-created_at']


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
