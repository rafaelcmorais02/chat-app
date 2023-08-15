from registration.models import Account
from django.shortcuts import get_object_or_404


def create_adm_account(**validated_data):
    password = validated_data.pop('password')
    account = Account(**validated_data)
    account.set_password(password)
    account.is_company_admin = True
    account.is_company_staff = False
    account.save()
    return account


def update_account(pk, **validated_data):
    account = get_object_or_404(Account, pk=pk)
    for k, v in validated_data.items():
        setattr(account, k, v)
    account.save()
    return account
