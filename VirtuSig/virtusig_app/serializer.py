from django.contrib.auth import authenticate
from rest_framework import serializers

from virtusig_app import models
from virtusig_app.models import Users


class TestSerializer(serializers.Serializer):
    Name = serializers.CharField()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoginUser
        fields = '__all__'


class LoginCreateSerializer(serializers.Serializer):
    email_id = serializers.CharField()


# class Login_dataSerializer(serializers.Serializer):
#     email_id = serializers.EmailField()
#     password = serializers.CharField()

class EnvelopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnvelopDisplay
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    user_email = serializers.CharField()
    password = serializers.CharField()


class UserTableSeriaizer(serializers.Serializer):
    class Meta:
        model = models.Users
        fields = ['user_email', 'password']


# class Envelop1Serializer(serializers.ModelSerializer):
#     email_id = serializers.EmailField()
#     sender_password = serializers.CharField(max_length=255)
#     recipient_id = serializers.CharField(max_length=255)
#     subjects = serializers.CharField(max_length=255)
#     cc = serializers.CharField(max_length=255)
#     body = serializers.CharField(max_length=255)
#     attachment = serializers.CharField(max_length=255)

class LoginUserSerializer(serializers.Serializer):
    user_email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, request):
        user_email = request.get('user_email')
        password = request.get('password')

        if user_email and password:
            users = Users.objects.filter(user_email=user_email).exists()
            if users:
                user = authenticate(request=self.context.get('request'),
                                    user_email=user_email, password=password)

            else:
                msg = {'detail': 'Phone number is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        request['user'] = user
        return request


class EmailsendingSerializer(serializers.Serializer):
    email_id = serializers.CharField()


class Update_PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('password', 'user_email')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = models.Users.objects.create_user(**validated_data)
        return user


class LoginDisplaySerializer(serializers.Serializer):
    user_email = serializers.CharField()
    password = serializers.CharField()
