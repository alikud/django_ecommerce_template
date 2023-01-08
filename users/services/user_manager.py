from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager for custom user model
    """

    def create_user(self, email, password=None):
        """ Create and return user"""
        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password, now is None')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        if email is None:
            raise TypeError('Superusers must have an email address.')
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user