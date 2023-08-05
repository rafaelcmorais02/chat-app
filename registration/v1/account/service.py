from registration.models import Account


def create_adm_account(**validated_data):
    password = validated_data.pop('password')
    account = Account(**validated_data)
    account.set_password(password)
    account.is_company_admin = True
    account.is_company_staff = False
    account.save()
    return account
