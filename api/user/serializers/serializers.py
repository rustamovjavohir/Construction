from rest_framework import serializers

from apps.user.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['url', 'id', 'phone', 'username', 'email', 'message', 'is_done', 'created_at', 'status']
