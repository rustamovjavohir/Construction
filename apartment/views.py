import json
import random

from django.db.models import Count, Max
from django.shortcuts import render
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apartment.models import *
from apartment.serializers import *
from rest_framework.generics import ListAPIView


class ApartmentListView(ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        max_floor = self.queryset.aggregate(Max('floor'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data_list = []
        for floor in range(1, max_floor.get('floor__max') + 1):
            double = queryset.filter(floor=floor, room_quantity=2)
            triple = queryset.filter(floor=floor, room_quantity=3)
            data_obj = {
                "double": self.get_serializer(double, many=True).data,
                "triple": self.get_serializer(triple, many=True).data,
            }
            data_list.append(data_obj)
        data = {
            "success": True,
            "data": data_list,
        }
        return Response(data=data, status=200)

    @swagger_auto_schema(operation_summary="Kvartiralar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(ApartmentListView, self).get(self, request, *args, **kwargs)


class ApartmentViewset(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = MyImageModelSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]
    # parser_classes = (MultiPartParser,)
    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]

    @swagger_auto_schema(operation_summary='Kvartiralar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(ApartmentViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Kvartiralar kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Kvartira malumotlarini yangilash")
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
    @swagger_auto_schema(operation_summary="Kvartira malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Kvartira malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(ApartmentViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Kvartira haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(ApartmentViewset, self).retrieve(self, request, *args, **kwargs)


class FloorListView(ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)
