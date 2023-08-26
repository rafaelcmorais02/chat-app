from rest_framework.authtoken.models import Token
from authentication.v1.user.serializers import TokenResponseSerializer, PasswordRedefinitionResponseSerializer
from rest_framework.exceptions import ValidationError, PermissionDenied
from django.shortcuts import get_object_or_404
from ...models import User


def get_or_create_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return TokenResponseSerializer(instance=token).data


def set_user_password(**validated_data):
    user = get_object_or_404(User, email=validated_data.get('username'))
    if not user.password_redefinition:
        raise PermissionDenied({
            'message': 'User is not allowed to redefine password '
        })
    is_valid_pw = user.check_password(validated_data.get('old_password'))
    if not is_valid_pw:
        raise ValidationError({
            'message': 'The current password is not correct'
        })
    user.set_password(validated_data.get('password'))
    user.password_redefinition = False
    user.save()
    response_data = {
        'message': 'password was redefined'
    }
    response_serialized = PasswordRedefinitionResponseSerializer(data=response_data)
    response_serialized.is_valid(raise_exception=True)
    return response_serialized.validated_data
