from rest_framework.authtoken.models import Token
from authentication.v1.user.serializers import TokenSerializer
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404
from ...models import User


def get_or_create_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return TokenSerializer(instance=token).data


def set_user_password(**validated_data):
    user = get_object_or_404(User, email=validated_data.get('username'))
    is_valid_pw = user.check_password(validated_data.get('old_password'))
    if not is_valid_pw:
        raise ValidationError({
            'message': 'The current password is not correct'
        })
    user.set_password(validated_data.get('password'))
    user.password_redefinition = False
    user.save()
