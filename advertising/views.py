from django.db import transaction
from django.http import Http404, HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertising.models import Advertising
from advertising.serializers import AdvertisingSerializer
from advertising.utils import custom_404_object_data


class AdvertisingListView(ListAPIView):
    queryset = Advertising.objects.filter(is_deleted=False)
    serializer_class = AdvertisingSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

    @swagger_auto_schema(operation_summary="Reklamalar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(AdvertisingListView, self).get(self, request, *args, **kwargs)


class AdvertisingViewset(ModelViewSet):
    queryset = Advertising.objects.filter(is_deleted=False)
    serializer_class = AdvertisingSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        obj = queryset.filter(**filter_kwargs).first()

        self.check_object_permissions(self.request, obj)

        return obj

    @swagger_auto_schema(operation_summary='Reklamalar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        data = {
            "success": True,
            "status_code": 200,
            "data": serializer.data,
        }
        return Response(data=data, status=200)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = {
            "success": True,
            "status_code": 201,
            "data": serializer.data,
        }
        headers = self.get_success_headers(serializer.data)
        return Response(data=data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            data = {
                "success": True,
                "status_code": 201,
                "data": serializer.data,
            }
        else:
            data = custom_404_object_data()
        return Response(data=data, status=200)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Reklama malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.is_deleted = True
            instance.save()
            data = {
                "success": True,
                "status_code": 204,
                "data": instance.id,
            }
        else:
            data = custom_404_object_data()
        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Reklama haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance)
            data = {
                "success": True,
                "status_code": 200,
                "data": serializer.data,
            }
        else:
            data = custom_404_object_data()
        return Response(data=data, status=status.HTTP_200_OK)
