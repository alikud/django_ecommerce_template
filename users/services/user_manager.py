from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """
    
    def create_user(self, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """

        if email is None:
            raise TypeError('Users must have an email address.')
        
        if password is None:
            raise TypeError('Users must have a password, now is None')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    

    
    
