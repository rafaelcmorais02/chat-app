from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError, PermissionDenied, AuthenticationFailed
from rest_framework.authtoken.models import Token
from authentication.v1.user.serializers import TokenResponseSerializer, PasswordRedefinitionResponseSerializer, UserResponseSerializer
from authentication.models import User
from authentication.integrations.google import Google


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


def get_or_create_user(full_name, email, password=None, **kwargs):
    if not email:
        raise ValueError({'message': 'User must have an email address'})
    user = User.objects.filter(email=email).last()
    if not user:
        user = User.objects.create(full_name=full_name, email=email)
    user.set_password(password)
    return UserResponseSerializer(instance=user).data


def get_google_user_details(auth_token):
    user_data = Google.validate(auth_token)
    try:
        user_data['sub']
    except:
        raise ValidationError({
            'message': 'The token is invalid or expired. Please login again.'
        })

    if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
        raise AuthenticationFailed({
            'message': 'oops, who are you?'
        })

    return {
        'user_id': user_data['sub'],
        'email': user_data['email'],
        'full_name': user_data['name'],
    }
