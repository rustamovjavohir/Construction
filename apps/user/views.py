from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.user.models import User
from apps.user.serializers import UserSerializer

# Create your views here.


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]

    @swagger_auto_schema(operation_summary='Foydalanuvchilar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(UserViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Foydalanuvchi kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Foydalanuvchi malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Foydalanuvchi malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Foydalanuvchi malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(UserViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Foydalanuvchi haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(UserViewset, self).retrieve(self, request, *args, **kwargs)
