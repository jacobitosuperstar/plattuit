'''Custom user model'''

# Create your models here.
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
# Local imports
from plattuit.utils import time_zone


class MyAccountManager(BaseUserManager):
    '''Custom user model'''
    def create_user(
        self,
        email: str,
        username: str,
        password: str = None
    ):
        '''User creator'''
        if not email:
            raise ValueError('Users Must Have an Email Address')
        if not username:
            raise ValueError('Users Must Have an Username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        username: str,
        password: str,
    ):
        '''superuser creator'''
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


# class Account(AbstractBaseUser, PermissionsMixin):
class Account(AbstractBaseUser):
    '''Custom user model. Logging with the email instead of the username.'''

    email = models.EmailField(
        max_length=120,
        unique=True,
        verbose_name='correo electrónico',
    )

    username = models.CharField(
        max_length=30,
        verbose_name='Nombre de usuario',
    )

    date_joined = models.DateTimeField(
        default=time_zone,
        verbose_name='fecha de creación de cuenta',
    )

    last_login = models.DateTimeField(
        verbose_name='último logueo',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='es activo?',
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='es empleado',
    )

    is_admin = models.BooleanField(
        default=False,
        verbose_name='es administrador?',
    )

    # LOGIN FIELDS
    USERNAME_FIELD = 'email'

    # REQUIRED FIELDS
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    # Save method
    def save(self, *args, **kwargs):
        self.last_login = time_zone()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'
        verbose_name = ('cuenta')
        verbose_name_plural = ('cuentas')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        '''Does the user have a specific permission?'''
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        'Does the user have permissions to view the app `app_label`?'
        # Simplest possible answer: Yes, always
        return True
