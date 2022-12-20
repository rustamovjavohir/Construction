import threading

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from apps.sendEmail.serializers import SendMessageSerializer, EmailSerializer
from apps.sendEmail.models import Email


class SendEmail(APIView):
    def post(self, request):
        serializer = SendMessageSerializer(request.data)
        subject = serializer.data.get('subject')
        message = serializer.data.get('message')
        from_email = serializer.data.get('email')
        recipient_list = [settings.RECIPIENT_ADDRESS]
        # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
        send_email_thread = threading.Thread(target=send_mail, args=(subject, message, from_email, recipient_list))
        send_email_thread.start()
        Email.objects.create(**serializer.data, recipient=settings.RECIPIENT_ADDRESS)
        data = {
            'success': True,
            'status_sode': 200
        }
        return Response(data=data, status=200)


class EmailListView(ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)


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
