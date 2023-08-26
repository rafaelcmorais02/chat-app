from rest_framework.exceptions import ValidationError
from registration.models import Company
from registration.v1.company.serializers import CompanyResponseSerializer
from registration.v1.interface import update_account_with_company


def create_company(request, **validated_data):
    if request.user.account.company:
        raise ValidationError({
            'message': 'Account already is associated with a company'
        })
    company = Company.objects.create(**validated_data)
    update_account_with_company(pk=request.user.id, company=company)
    return CompanyResponseSerializer(instance=company).data
