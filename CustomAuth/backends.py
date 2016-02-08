from django.conf import settings
from .models import User


class EmailOrUsernameModelBackend(object):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email__iexact': username}
        else:
            kwargs = {'username__iexact': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None