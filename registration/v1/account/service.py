from registration.models import Account
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


def create_adm_account(**validated_data):
    password = validated_data.pop('password')
    account = Account(**validated_data)
    account.set_password(password)
    account.is_company_admin = True
    account.is_company_staff = False
    account.save()
    return account


def create_staff_account(company, **validated_data):
    company_cnpj = company.cnpj
    cpf = validated_data.get('cpf')
    account = Account(**validated_data)
    account.is_company_admin = False
    account.is_company_staff = True
    account.password_redefinition = True
    account.company = company
    password = f'{cpf[0:3]}{company_cnpj[0:3]}'
    account.set_password(password)
    account.save()
    return account, password


def update_account(pk, **validated_data):
    account = get_object_or_404(Account, pk=pk)
    for k, v in validated_data.items():
        setattr(account, k, v)
    account.save()
    return account


def get_account(pk, user):
    account = get_object_or_404(Account, pk=pk)
    if account.id != user.id:
        raise PermissionDenied({
            'message': 'user is forbidden to perform action'
        })
    return account
