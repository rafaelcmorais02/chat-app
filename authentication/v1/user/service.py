from rest_framework.authtoken.models import Token


def get_or_create_token(user):
    return Token.objects.get_or_create(user=user)
