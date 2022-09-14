from django.contrib.auth.models import BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('User must have a email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user
