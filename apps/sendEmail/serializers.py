from rest_framework import serializers
from apps.sendEmail.models import Email


class SendMessageSerializer(serializers.Serializer):
    subject = serializers.CharField(allow_null=True)
    message = serializers.CharField(max_length=250)
    email = serializers.EmailField(max_length=250)
    phone = serializers.CharField(max_length=250, allow_null=True)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
