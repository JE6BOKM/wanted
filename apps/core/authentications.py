from django.contrib.auth import get_user_model

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class AutoLoginAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        try:
            user = User.objects.get(username="admin")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user, None)
