import time
from collections import OrderedDict
from http.client import HTTPResponse

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.db.models import Max
from django.db import transaction
from django.shortcuts import render
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.advertising.utils import custom_404_object_data
from apps.apartment.models import *
from api.apartment.serializers.serializers import ApartmentSerializer, FloorSerializer, MyImageModelSerializer
from rest_framework.generics import ListAPIView
from django.http import JsonResponse

from apps.user.permissions import RadiusPermission
from config.settings import CACHE_TTL


class ApartmentListView(ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    # permission_classes = [RadiusPermission]
    parser_classes = (JSONParser,)

    def list(self, request, *args, **kwargs):
        time.sleep(2)
        queryset = self.filter_queryset(self.get_queryset())
        max_floor = self.queryset.aggregate(Max('floor'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data_list = []
        if max_floor.get('floor__max') is None:
            max_floor['floor__max'] = 0
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
            "status_code": 200,
            "data": data_list,
        }
        return Response(data=data, status=200)

    @method_decorator(cache_page(CACHE_TTL, key_prefix='apartment_list'))  # cache requested url for 15 minutes
    @method_decorator(vary_on_cookie)
    @extend_schema(summary="Kvartiralar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(ApartmentListView, self).get(self, request, *args, **kwargs)

    def handle_exception(self, exc):
        if not isinstance(exc, AttributeError):
            return JsonResponse(OrderedDict([
                ('success', False),
                ('status_code', exc.status_code),
                ('detail', exc.detail),
                ('data', [])
            ]), status=200)


class ApartmentViewset(ModelViewSet):
    queryset = Apartment.objects.filter(is_deleted=False)
    permission_classes = [AllowAny, ]
    serializer_class = MyImageModelSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

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
        obj = self.queryset.filter(**filter_kwargs).first()
        self.check_object_permissions(self.request, obj)

        return obj

    @transaction.atomic
    @extend_schema(summary="Kvartiralar kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            "success": True,
            "status_code": 201,
            "data": serializer.data,
        }
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)

    @transaction.atomic
    @extend_schema(summary="Kvartira malumotlarini yangilash")
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
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(summary="Kvartira malumotlarini o'chirish")
    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.is_deleted = True
            instance.save()
            data = {
                "success": True,
                "status_code": 204,
                "data": instance.id
            }
        else:
            data = custom_404_object_data()
        return Response(data=data, status=200)

    @extend_schema(summary="Kvartira haqidagi malumotlarini chop etish (retrieve)")
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
        return Response(data=data, status=200)

    @extend_schema(summary='Kvartiralar royhatini chop etish')
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
    @extend_schema(summary="Kvartira malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class FloorListView(ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)

    @extend_schema(summary="Qavatlar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(FloorListView, self).get(self, request, *args, **kwargs)


class CustomAdminView(View):
    queryset = Floor.objects.all()

    @extend_schema(summary="Qavatlar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, pk):
        obj = self.queryset.filter(id=pk).first()
        context = {
            "name": obj.name,
        }
        return render(request, 'sometemplate.html', context=context)


def get_meta(request):
    print(request.META)
    return HTTPResponse("Hello world")
