from django.db import transaction
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertising.models import Advertising
from advertising.serializers import AdvertisingSerializer


class AdvertisingListView(ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

    @swagger_auto_schema(operation_summary="Reklamalar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(AdvertisingListView, self).get(self, request, *args, **kwargs)


class AdvertisingViewset(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer

    @swagger_auto_schema(operation_summary='Reklamalar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(AdvertisingViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama malumotlarini yangilash")
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
    @swagger_auto_schema(operation_summary="Reklama malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Reklama malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(AdvertisingViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Reklama haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(AdvertisingViewset, self).retrieve(self, request, *args, **kwargs)
