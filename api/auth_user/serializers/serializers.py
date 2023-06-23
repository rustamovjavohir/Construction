from collections import OrderedDict
from datetime import datetime

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from apps.auth_user.models import CustomUser


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
        exp = self.get_token(self.user).access_token.get('exp')
        iat = self.get_token(self.user).access_token.get('iat')
        data['iat'] = datetime.fromtimestamp(iat)
        data['exp'] = datetime.fromtimestamp(exp)
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
    firstName = serializers.CharField(source='first_name', )
    lastName = serializers.CharField(source='last_name', )
    telegramId = serializers.IntegerField(source='telegram_id', )
    isSuperuser = serializers.BooleanField(source='is_superuser', )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'firstName', 'lastName', 'email', 'photo', 'telegramId', 'isSuperuser']

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
