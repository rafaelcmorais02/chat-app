import pytest
from rest_framework.test import APIClient
from registration.models import Account
from registration.models import Company
from subscription.models import Plan
from rest_framework.authtoken.models import Token


def account_adm_token(account_adm):
    token, _ = Token.objects.get_or_create(user=account_adm)
    return token.key


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def plan():
    payload = {
        'name': 'Basico',
        'max_adm_account': 1,
        'max_staff_account': 1
    }
    return Plan.objects.create(**payload)


@pytest.fixture
def company(plan):
    payload = {
        'plan': plan,
        'name': 'fortera',
        'phone_number': '5535997365546',
        'cnpj': '16507703000290'
    }
    return Company.objects.create(**payload)


@pytest.fixture
def account_adm(company):
    payload = {
        'first_name': 'teste',
        'last_name': 'teste',
        'phone_number': '5537982365547',
        'email': 'adm2@email.com',
        'cpf': '09479657696',
        'password': 'rafael',
        'is_company_admin': True,
        'company': company
    }
    return Account.objects.create(**payload)


@pytest.mark.django_db
def test_create_adm_account(api_client):
    payload = {
        'first_name': 'adm',
        'last_name': 'adm',
        'phone_number': '5537982365546',
        'email': 'adm1@email.com',
        'cpf': '09479657694',
        'password': 'rafael',
        'password_validation': 'rafael'
    }
    response = api_client.post('/api/v1/accounts/adm/', payload, format='json')
    assert response.status_code == 201
    assert Account.objects.count() == 1


@pytest.mark.django_db
def test_create_staff_account(api_client, account_adm):
    payload = {
        'first_name': 'staff',
        'last_name': 'staff',
        'phone_number': '5537982365546',
        'email': 'staff1@email.com',
        'cpf': '09479657695'
    }
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + account_adm_token(account_adm=account_adm))
    response = api_client.post('/api/v1/accounts/staff/', payload, format='json')
    assert response.status_code == 201
    assert Account.objects.count() == 2


@pytest.mark.django_db
def test_create_staff_account_error(api_client, account_adm):
    account_adm.company = None
    account_adm.save()
    payload = {
        'first_name': 'staff',
        'last_name': 'staff',
        'phone_number': '5537982365546',
        'email': 'staff1@email.com',
        'cpf': '09479657695'
    }
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + account_adm_token(account_adm=account_adm))
    response = api_client.post('/api/v1/accounts/staff/', payload, format='json')
    assert response.status_code == 400
    assert 'message' in response.data


@pytest.mark.django_db
def test_update_account(api_client, account_adm):
    payload = {
        'first_name': 'adm',
    }
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + account_adm_token(account_adm=account_adm))
    response = api_client.put(f'/api/v1/accounts/adm/{str(account_adm.id)}', payload, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_account(api_client, account_adm):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + account_adm_token(account_adm=account_adm))
    response = api_client.get(f'/api/v1/accounts/{str(account_adm.id)}', format='json')
    assert response.status_code == 200
    assert 'id' in str(response.content)
