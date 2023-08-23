from registration.models import Company
from registration.v1.company.serializers import CompanySerializer
from registration.v1.interface import update_account_with_company


def create_company(request, **validated_data):
    company = Company.objects.create(**validated_data)
    update_account_with_company(pk=request.user.id, company=company)
    return CompanySerializer(instance=company).data
