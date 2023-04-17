import threading
from collections import OrderedDict

from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from api.sendEmail.exceptions.exceptions import CustomException
from api.sendEmail.filters.filters import EmailFilter
from api.sendEmail.serializers.serializers import SendMessageSerializer, EmailSerializer
from apps.sendEmail.models import Email
from config import settings


class SendEmail(GenericAPIView):
    serializer_class = SendMessageSerializer
    queryset = Email.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.validated_data
        serializer.save()

        send_email_thread = threading.Thread(target=send_mail, args=(serializer_data.get('subject'),
                                                                     serializer_data.get('message'),
                                                                     serializer_data.get('email'),
                                                                     [settings.RECIPIENT_ADDRESS]))
        send_email_thread.start()

        data = OrderedDict([
            ('success', True),
            ('statusCode', 200),
            ('result', serializer_data)
        ])
        return JsonResponse(data=data, status=200)

    def get_serializer(self, *args, **kwargs):
        return SendMessageSerializer(*args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, CustomException):
            return Response(status=status.HTTP_200_OK, data={
                'success': False,
                'statusCode': exc.status_code,
                'result': '',
                'error': exc.detail
            })


class EmailListView(ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = EmailFilter
    search_fields = ['subject', 'email']
    ordering_fields = ['created_at', 'id']


class EmailDestroyAPIView(DestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            data = {
                "success": False,
                "status_code": 404,
                "status": "The message has already been deleted",
                "id": instance.id,
            }
        else:
            instance.is_deleted = True
            instance.save()
            data = {
                "success": True,
                "status_code": 200,
                "status": "Message successfully deleted",
                "id": instance.id,
            }
        return Response(status=200, data=data)


class EmailDetail(RetrieveAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            "success": True,
            "status_code": 200,
            "data": serializer.data,
        }
        return Response(data)
