from collections import OrderedDict

from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from api.sendEmail.serializers.serializers import SendMessageSerializer, EmailSerializer
from apps.sendEmail.models import Email


class SendEmail(APIView):
    serializer_class = SendMessageSerializer

    def get_serializer(self, *args, **kwargs):
        return SendMessageSerializer(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.validated_data
        serializer.save()

        data = OrderedDict([
            ('success', True),
            ('statusCode', 200),
            ('result', serializer_data)
        ])
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
