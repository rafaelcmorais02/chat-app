import pytest
from rest_framework.test import APIClient
from subscription.models import Plan
from registration.models import Account, Company
from rest_framework.authtoken.models import Token


def account_adm_token(account_adm):
    token, _ = Token.objects.get_or_create(user=account_adm)
    return token.key


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def account_adm():
    payload = {
        'first_name': 'teste',
        'last_name': 'teste',
        'phone_number': '5537982365547',
        'email': 'adm2@email.com',
        'cpf': '09479657696',
        'password': 'rafael',
        'is_company_admin': True,
    }
    return Account.objects.create(**payload)


@pytest.fixture
def plan():
    payload = {
        'name': 'Basico',
        'max_adm_account': 1,
        'max_staff_account': 1
    }
    return Plan.objects.create(**payload)


@pytest.mark.django_db
def test_create_company(api_client, account_adm, plan):
    payload = {
        'plan': str(plan.id),
        'name': 'fortera',
        'phone_number': '5535997365546',
        'cnpj': '16507703000290'
    }
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + account_adm_token(account_adm=account_adm))
    response = api_client.post('/api/v1/companies/', payload, format='json')
    assert response.status_code == 201
    assert Company.objects.count() == 1
