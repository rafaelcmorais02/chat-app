from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from .service import get_or_create_token, set_user_password


class PasswordSerializer(serializers.Serializer):
    username = serializers.EmailField()
    old_password = serializers.CharField()
    password = serializers.CharField()
    password_validation = serializers.CharField()

    def validate(self, attrs):
        if (attrs.get('password') != attrs.get('password_validation')):
            raise serializers.ValidationError({
                'message': 'the passwords must match'
            })
        attrs.pop('password_validation')
        return super().validate(attrs)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.password_redefinition:
            return Response(data={
                'message': 'User must redefine password'
            }, status=200)
        token, created = get_or_create_token(user=user)
        return Response(data={
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)


@swagger_auto_schema(method='POST', request_body=PasswordSerializer, operation_description='Redefine a user password')
@api_view(['POST'])
def password_redefinition_view(request):
    data = request.data
    serializer = PasswordSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    set_user_password(**validated_data)
    return Response(data={
        'message': 'password was redefined'
    }, status=201)
