import threading

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from apps.sendEmail.models import Email


class SendMessageSerializer(serializers.Serializer):
    subject = serializers.CharField(allow_null=True)
    message = serializers.CharField(max_length=250)
    email = serializers.EmailField(max_length=250)
    phone = serializers.CharField(max_length=250, allow_null=True)

    def save(self, **kwargs):
        subject = self.validated_data.get('subject')
        message = self.validated_data.get('message')
        from_email = self.validated_data.get('email')
        recipient_list = [settings.RECIPIENT_ADDRESS]
        send_email_thread = threading.Thread(target=send_mail, args=(subject, message, from_email, recipient_list))
        send_email_thread.start()
        Email.objects.create(**self.validated_data, recipient=settings.RECIPIENT_ADDRESS)

    def validate(self, attrs):
        data = super(SendMessageSerializer, self).validate(attrs)
        data.pop('phone')
        return data

    def to_representation(self, instance):
        data = super(SendMessageSerializer, self).to_representation(instance)
        data.pop('phone')
        return data


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
