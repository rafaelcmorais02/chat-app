# Generated by Django 4.2 on 2023-07-22 19:30

import dao.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Ativo?")),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Nome da empresa"),
                ),
                (
                    "cnpj",
                    dao.fields.CnpjField(
                        max_length=14, unique=True, verbose_name="CNPJ"
                    ),
                ),
                (
                    "phone_number",
                    dao.fields.PhoneField(
                        max_length=13, unique=True, verbose_name="Número de telefone"
                    ),
                ),
                ("max_admin_user", models.IntegerField(default=1)),
                ("max_staff_user", models.IntegerField(default=1)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Ativo?")),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="Primeiro nome"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Sobrenome"),
                ),
                (
                    "phone_number",
                    dao.fields.PhoneField(
                        max_length=13, verbose_name="Número de telefone"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False, verbose_name="Colaborador da equipe?"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Super usuário?"),
                ),
                (
                    "is_company_admin",
                    models.BooleanField(
                        default=False, verbose_name="Admin da empresa?"
                    ),
                ),
                (
                    "is_company_staff",
                    models.BooleanField(
                        default=False, verbose_name="Colaborador da empresa?"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.company",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
