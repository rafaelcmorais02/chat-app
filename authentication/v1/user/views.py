from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .service import get_or_create_token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = get_or_create_token(user=user)
        return Response(data={
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)
