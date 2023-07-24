from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,
                    user_email: str,
                    password: str,
                    is_staff=False,
                    is_superuser=False,
                    **extra_fields

                    ) -> "Users":
        if not user_email:
            raise ValueError("User must have an email")

        users = self.model(user_email=user_email, **extra_fields)
        users.set_password(password)
        users.is_active = True
        users.is_staff = is_staff
        users.is_superuser = is_superuser
        users.save()

        return users

    def create_superuser(
            self, user_email, password, **extra_fields
    ) -> "Users":
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        users = self.create_user(
            user_email,
            password,
            **extra_fields
        )
        users.save()
        return users


# Create your models here.
# class Users(AbstractUser):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=255)
#     user_phone = models.CharField(max_length=255, unique=True)
#     user_image = models.CharField(max_length=255)
#     # otp_value = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255)
#     is_verified = models.CharField(max_length=255)
#     reg_date = models.DateTimeField(auto_now_add=True)
#     user_email = models.CharField(max_length=255, unique=True)
#     dob = models.DateField(blank=True, null=True)
#     user_password = models.CharField(max_length=255)
#     gender = models.CharField(max_length=1, blank=True, null=True)
#     first_login = models.BooleanField(blank=True, default=False)
#
#     username = None
#
#     objects = UserManager()
#     USERNAME_FIELD = "user_email"
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         # managed = False
#         db_table = 'users'


class Users(AbstractUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_phone = models.CharField(unique=True, max_length=255, blank=True, null=True)
    user_image = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    is_verified = models.CharField(max_length=255)
    reg_date = models.DateTimeField(auto_now_add=True)
    user_email = models.CharField(unique=True, max_length=255)
    dob = models.DateField(blank=True, null=True)
    user_password = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, blank=True, null=True)
    first_login = models.IntegerField(blank=True, null=True)

    username = None

    objects = UserManager()
    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'Users'

class LoginUser(models.Model):
    email_id = models.CharField(primary_key=True, max_length=255)
    user_password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_user'


class VirtusigLogin(models.Model):
    email_id = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)




# class Envelop_emailsending(models.Model):
#     email_id = models.EmailField(primary_key=True)
#     sender_password = models.CharField(max_length=255)
#     recipient_id = models.CharField(max_length=255)
#     subjects = models.CharField(max_length=255)
#     cc = models.CharField(max_length=255)
#     body = models.CharField(max_length=255)
#     attachment = models.FilePathField()
#
#     class Meta:
#         managed = True
#         db_table = 'envelop'


# class Envelop_Display(models.Model):
#     email_id = models.EmailField(primary_key=True)
#     sender_password = models.CharField(max_length=255)
#     recipient_id = models.CharField(max_length=255)
#     subjects = models.CharField(max_length=255)
#     cc = models.CharField(max_length=255)
#     body = models.CharField(max_length=255)
#     attachment = models.FilePathField()
#
#     class Meta:
#         managed = False
#         db_table = 'envelop_display'

class EnvelopDisplay(models.Model):
    email_id = models.CharField(max_length=255, blank=True, null=True)
    sender_password = models.CharField(max_length=255, blank=True, null=True)
    recepient_id = models.CharField(max_length=255, blank=True, null=True)
    subjects = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'envelop_display'


class ForgotPassword(models.Model):
    user_email = models.OneToOneField(Users, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'forgot_password'
