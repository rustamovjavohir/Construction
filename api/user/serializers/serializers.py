from collections import OrderedDict

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken

from apps.user.models import User
from apps.auth_user.models import CustomUser


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'phone', 'username', 'email', 'message', 'is_done', 'created_at', 'status']


class CustomObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomObtainPairSerializer, cls).get_token(user)
        token['is_superuser'] = user.is_superuser
        return token

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['success'] = "Ok"
        return response

    def validate(self, attrs):
        data = super().validate(attrs)
        response = OrderedDict([
            ('success', True),
            ('result', data)
        ])
        return response


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or expired')
    }

    def validate(self, attrs):
        data = super().validate(attrs)
        response = OrderedDict([
            ('success', True),
            ('result', data)
        ])
        return response


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class CustomUserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'photo', 'telegram_id', 'is_superuser']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        data = OrderedDict([
            ('success', True),
            ('statusCode', 200),
            ('result', response)
        ])
        return data

    def validate(self, attrs):
        data = super().validate(attrs)
        response = OrderedDict([
            ('result', data)
        ])
        return response

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('result', {}).get('username', instance.username)
        instance.first_name = validated_data.get('result', {}).get('first_name', instance.first_name)
        instance.last_name = validated_data.get('result', {}).get('last_name', instance.last_name)
        instance.email = validated_data.get('result', {}).get('email', instance.email)
        instance.photo = validated_data.get('result', {}).get('photo', instance.photo)
        instance.telegram_id = validated_data.get('result', {}).get('telegram_id', instance.telegram_id)
        instance.is_superuser = validated_data.get('result', {}).get('is_superuser', instance.is_superuser)
        instance.save()
        return instance

    def save(self, **kwargs):
        return super().save(**kwargs)
