from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from registration.models import Company
from .service import create_company


class CompanyAPIView(APIView):
    class CompanySerializer(ModelSerializer):
        class Meta:
            model = Company
            fields = '__all__'

    def post(self, request):
        data = request.data
        serializer = self.CompanySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        company = create_company(**validated_data)
        return Response(data=self.CompanySerializer(instance=company).data, status=201)
