import threading

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from api.sendEmail.exceptions.exceptions import CustomException
from apps.sendEmail.models import Email
from django.utils.translation import gettext_lazy as _

from config import settings


def greater_then_10(value: str):
    if len(value) > 10:
        raise ValidationError("Subject greater than 10")


class SendMessageSerializer(serializers.ModelSerializer):

    def validate_subject(self, value: str):
        if value.startswith('Salom'):
            raise CustomException("Subject startswith Salom")
        return value

    def validate(self, attrs):
        data = super(SendMessageSerializer, self).validate(attrs)
        data.pop('phone')
        return data

    class Meta:
        model = Email
        fields = ['subject', 'message', 'email', 'recipient', 'phone']

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Email.objects.all(),
        #         fields=['subject', 'message'],
        #         message=_("Subject and message fields must be unique")
        #     )
        # ]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
