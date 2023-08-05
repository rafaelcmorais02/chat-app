from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from registration.models import Account
from .service import create_adm_account


class AdmAccountAPIView(APIView):
    class AdmAccountSerializer(ModelSerializer):
        password_validation = serializers.CharField(write_only=True)

        class Meta:
            model = Account
            fields = '__all__'

        def validate(self, attrs):
            if (attrs.get('password') != attrs.get('password_validation')):
                raise ValidationError({
                    'message': 'the passwords must match'
                })
            attrs.pop('password_validation')
            return super().validate(attrs)

    def post(self, request):
        data = request.data
        serializer = self.AdmAccountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        account = create_adm_account(**validated_data)
        return Response(data=self.AdmAccountSerializer(instance=account).data, status=201)
