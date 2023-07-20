from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from dao.db import Base


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email=email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email=email), **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser, Base):
    first_name = models.CharField(verbose_name='Primeiro nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    phone_number = models.CharField(verbose_name='Número de telefone', max_length=12)
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(verbose_name='Membro da equipe?', default=False)
    is_superuser = models.BooleanField(verbose_name='Super usuário?', default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
