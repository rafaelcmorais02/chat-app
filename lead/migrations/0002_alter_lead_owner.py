# Generated by Django 4.2 on 2023-08-23 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0004_account_cpf"),
        ("lead", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="leads",
                to="registration.account",
                verbose_name="Dono do lead",
            ),
        ),
    ]
