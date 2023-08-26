from rest_framework.serializers import ModelSerializer
from registration.models import Company
from dao.serializers import ReadOnlyModelSerializer


class CompanyResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CreateCompanyRequestSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
