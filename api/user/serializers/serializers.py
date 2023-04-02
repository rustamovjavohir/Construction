from collections import OrderedDict

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken

from apps.user.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['url', 'id', 'phone', 'name', 'email', 'message', 'is_telegram', 'is_web',
                  'is_done', 'created_at', 'status']


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    # default_error_messages = {
    #     'no_active_account': 'No active account found with the specified details',
    #     'inactive_account': 'User account is disabled.',
    # }

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
