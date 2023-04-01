import threading

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from apps.sendEmail.models import Email


def greater_then_10(value: str):
    if len(value) > 10:
        raise ValidationError("Subject greater than 10")


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
        # send_email_thread = threading.Thread(target=send_mail, args=(subject, message, from_email, recipient_list))
        # send_email_thread.start()
        # Email.objects.create(**self.validated_data, recipient=settings.RECIPIENT_ADDRESS)

    def validate_subject(self, value: str):
        if value.startswith('Salom'):
            raise ValidationError("Subject startswith Salom")
        return value

    def validate(self, attrs):
        data = super(SendMessageSerializer, self).validate(attrs)
        data.pop('phone')
        return data

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Email.objects.all(),
                fields=['subject', 'message'],
                message="Subject and message fields must be unique"
            )
        ]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
