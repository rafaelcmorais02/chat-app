from registration.models import Account
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from registration.v1.account.serializers import AccountSerializer


def create_adm_account(**validated_data):
    password = validated_data.pop('password')
    account = Account(**validated_data)
    account.set_password(password)
    account.is_company_admin = True
    account.is_company_staff = False
    account.save()
    return AccountSerializer(instance=account).data


def create_password_account_staff(account_cpf, company_cnpj):
    return f'{account_cpf[0:3]}{company_cnpj[0:3]}'


def create_staff_account(company, password, **validated_data):
    account = Account(**validated_data)
    account.is_company_admin = False
    account.is_company_staff = True
    account.password_redefinition = True
    account.company = company
    account.set_password(password)
    account.save()
    return AccountSerializer(instance=account).data


def update_account(pk, **validated_data):
    account = get_object_or_404(Account, pk=pk)
    for k, v in validated_data.items():
        setattr(account, k, v)
    account.save()
    return AccountSerializer(instance=account).data


def get_account(pk, user):
    account = get_object_or_404(Account, pk=pk)
    if account.id != user.id:
        raise PermissionDenied({
            'message': 'user is forbidden to perform action'
        })
    return AccountSerializer(instance=account).data
