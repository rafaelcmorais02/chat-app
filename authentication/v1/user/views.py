from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from authentication.v1.user.serializers import PasswordSerializer
from drf_yasg.utils import swagger_auto_schema
from .service import get_or_create_token, set_user_password


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.password_redefinition:
            return Response(data={
                'message': 'User must redefine password'
            }, status=400)
        token = get_or_create_token(user=user)
        return Response(data={
            'token': token.get('key'),
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
