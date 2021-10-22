from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class CustomManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            message_ = ('Email not provided', )
            raise ValueError(message_)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            message_ = ('Email not provided', )
            raise ValueError(message_)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(
        max_length=25, blank=True
    )

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} -> {self.id}"

    def create_activation_code(self):
        code = get_random_string(
            length=10,
            allowed_chars='1234567890#$%!?_'
        )
        self.activation_code = code









# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from django.utils.crypto import get_random_string
#
#
# class CustomManager(BaseUserManager):
#
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             msg_ = ('Email is not provided')
#             raise ValueError(msg_)
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.create_activation_code()
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         if not email:
#             msg_ = ('Email is not provided')
#             raise ValueError(msg_)
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.is_staff = True
#         user.is_active = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=25, blank=True)
#     objects = CustomManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def str(self) -> str:
#         return f'{self.email} -> {self.id}'
#
#     def create_activation_code(self):
#         code = get_random_string(length=10, allowed_chars='1234567890#$%!?_')
#         self.activation_code = code
