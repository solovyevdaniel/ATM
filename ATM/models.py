from django.db import models
from django.contrib.auth.models import AbstractUser  # BaseUserManager
from django.contrib.auth.admin import UserAdmin


class CustonAdmin(UserAdmin):
    pass


class CustomUser(AbstractUser):
    quantity_login = models.IntegerField(default=0)

# card_number = models.IntegerField(unique=True)
#     USERNAME_FIELD = 'card_number'
#
#
# class MyUserManager(BaseUserManager):
#     def get_by_natural_key(self, card_number, password):
#         return self.get(card_number=card_number, password=password)
#
#     def create_user(self, card_number, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not card_number:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#                 card_number,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, card_number, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(card_number,
#                                 password=password,
#                                 )
#
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
