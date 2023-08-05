from registration.models import Company


def create_company(**validated_data):
    company = Company.objects.create(**validated_data)
    return company
