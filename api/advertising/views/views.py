import base64

from django.db import transaction
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.advertising.models import Advertising
from api.advertising.serializers.serializers import AdvertisingSerializer, TemplateSerializer
from apps.advertising.utils import custom_404_object_data


class AdvertisingListView(ListAPIView):
    queryset = Advertising.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated, ]
    serializer_class = AdvertisingSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

    @extend_schema(summary="Reklamalar haqidagi malumotlar ro'yhatini chop etish (list)")
    def get(self, request, *args, **kwargs):
        return super(AdvertisingListView, self).get(self, request, *args, **kwargs)


class AdvertisingViewset(ModelViewSet):
    queryset = Advertising.objects.filter(is_deleted=False)
    serializer_class = AdvertisingSerializer
    permission_classes = [IsAuthenticated, ]

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

    @extend_schema(summary='Reklamalar royhatini chop etish')
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
    @extend_schema(summary="Reklama kirish")
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
    @extend_schema(summary="Reklama malumotlarini yangilash")
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
    @extend_schema(summary="Reklama malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @extend_schema(summary="Reklama malumotlarini o'chirish")
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

    @extend_schema(summary="Reklama haqidagi malumotlarini chop etish (retrieve)")
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


class TemplateView(APIView):
    serializer_class = TemplateSerializer

    def decode(self):
        a = "CjwhRE9DVFlQRSBodG1sPgo8aHRtbD4KPGhlYWQ+CjxtZXRhIGh0dHAtZXF1aXY9IkNvbnRlbnQtVHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PXV0Zi04IiAvPgogICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4NCiAgICAgICAgKiB7DQogICAgICAgIHBhZGRpbmc6IDA7DQogICAgICAgIG1hcmdpbjogMDsNCiAgICAgICAgLXdlYmtpdC1ib3gtc2l6aW5nOiBib3JkZXItYm94Ow0KICAgICAgICBib3gtc2l6aW5nOiBib3JkZXItYm94Ow0KICAgICAgICAtbW96LWJveC1zaXppbmc6IGJvcmRlci1ib3g7DQogICAgICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTsNCiAgICAgIH0NCiAgDQogICAgICBodG1sIHsNCiAgICAgICAgZm9udC1mYW1pbHk6ICJBcmltbyIsICJBcmlhbCI7DQogICAgICB9DQogIA0KICAgICAgOjotbW96LXNlbGVjdGlvbiB7DQogICAgICAgIGJhY2tncm91bmQ6ICNiM2Q0ZmM7DQogICAgICAgIHRleHQtc2hhZG93OiBub25lOw0KICAgICAgfQ0KICANCiAgICAgIDo6c2VsZWN0aW9uIHsNCiAgICAgICAgYmFja2dyb3VuZDogI2IzZDRmYzsNCiAgICAgICAgdGV4dC1zaGFkb3c6IG5vbmU7DQogICAgICB9DQogIA0KICAgICAgYm9keSB7DQogICAgICAgIHdpZHRoOiAyMzBtbTsNCiAgICAgICAgaGVpZ2h0OiAxMDAlOw0KICAgICAgICBtYXJnaW46IDAgYXV0bzsNCiAgICAgICAgcGFkZGluZzogMDsNCiAgICAgICAgZm9udC1zaXplOiAxMnB0Ow0KICAgICAgICBiYWNrZ3JvdW5kOiAjYjNkNGZjOw0KICAgICAgfQ0KICANCiAgICAgIC50ZXh0LS1yaWdodCB7DQogICAgICAgIHRleHQtYWxpZ246IHJpZ2h0Ow0KICAgICAgfQ0KICANCiAgICAgIC50ZXh0LS1sZWZ0IHsNCiAgICAgICAgdGV4dC1hbGlnbjogbGVmdDsNCiAgICAgIH0NCiAgDQogICAgICAudGV4dC0tY2VudGVyIHsNCiAgICAgICAgdGV4dC1hbGlnbjogY2VudGVyOw0KICAgICAgfQ0KICANCiAgICAgIC50ZXh0LS1zbWFsbGVyIHsNCiAgICAgICAgZm9udC1zaXplOiAxMnB4ICFpbXBvcnRhbnQ7DQogICAgICB9DQogIA0KICAgICAgLnRleHQtLXNtYWxsZXJfX2l0ZW0gew0KICAgICAgICBtYXJnaW4tYm90dG9tOiA0cHg7DQogICAgICB9DQogIA0KICAgICAgLnRleHQtLXNtYWxsIHsNCiAgICAgICAgZm9udC1zaXplOiAxNHB4ICFpbXBvcnRhbnQ7DQogICAgICB9DQogIA0KICAgICAgLnRleHQtLW1lZGl1bSB7DQogICAgICAgIGZvbnQtc2l6ZTogMTdweCAhaW1wb3J0YW50Ow0KICAgICAgfQ0KICANCiAgICAgIC50ZXh0LS1sYXJnZSB7DQogICAgICAgIGZvbnQtc2l6ZTogMjFweCAhaW1wb3J0YW50Ow0KICAgICAgfQ0KICANCiAgICAgIC5jb2xvci0tYmx1ZSB7DQogICAgICAgIGNvbG9yOiAjMDA0YTdmOw0KICAgICAgICAtd2Via2l0LXRleHQtc2l6ZS1hZGp1c3Q6IG5vbmU7DQogICAgICB9DQogIA0KICAgICAgLmNvbG9yLS1ncmV5IHsNCiAgICAgICAgY29sb3I6ICM3ZjdmN2Y7DQogICAgICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTsNCiAgICAgIH0NCiAgDQogICAgICAuY29sb3ItLWxpZ2h0LWdyZXkgew0KICAgICAgICBjb2xvcjogI2M5YzljOTsNCiAgICAgIH0NCiAgDQogICAgICAuY29sb3ItLWJsYWNrIHsNCiAgICAgICAgY29sb3I6ICMwMDAwMDA7DQogICAgICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTsNCiAgICAgIH0NCiAgDQogICAgICAuY29sb3ItLXdoaXRlIHsNCiAgICAgICAgY29sb3I6ICNmZmZmZmY7DQogICAgICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTsNCiAgICAgIH0NCiAgDQogICAgICAuYmctb3JhbmdlIHsNCiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogI2RlOGEzZSAhaW1wb3J0YW50Ow0KICAgICAgfQ0KICANCiAgICAgIC5iZy1ncmF5IHsNCiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogIzdmN2Y3ZiAhaW1wb3J0YW50Ow0KICAgICAgfQ0KICANCiAgICAgIC53LTEwMCB7DQogICAgICAgIHdpZHRoOiAxMDAlICFpbXBvcnRhbnQ7DQogICAgICB9DQogIA0KICAgICAgLmJvcmRlci1ub25lIHsNCiAgICAgICAgYm9yZGVyOiBub25lICFpbXBvcnRhbnQ7DQogICAgICB9DQogIA0KICAgICAgLm1haW4tcGFnZSB7DQogICAgICAgIHdpZHRoOiAyMTBtbTsNCiAgICAgICAgbWluLWhlaWdodDogMjk3bW07DQogICAgICAgIG1hcmdpbjogMTBtbSBhdXRvOw0KICAgICAgICBiYWNrZ3JvdW5kOiB3aGl0ZTsNCiAgICAgICAgLXdlYmtpdC1ib3gtc2hhZG93OiAwIDAgMC41Y20gcmdiYSgwLCAwLCAwLCAwLjUpOw0KICAgICAgICBib3gtc2hhZG93OiAwIDAgMC41Y20gcmdiYSgwLCAwLCAwLCAwLjUpOw0KICAgICAgfQ0KICANCiAgICAgIC5zdWItcGFnZSB7DQogICAgICAgIHBhZGRpbmc6IDYycHggMzdweCAyNXB4IDQ3cHg7DQogICAgICAgIGJhY2tncm91bmQtY29sb3I6ICNmZmZmZmYgIWltcG9ydGFudDsNCiAgICAgIH0NCiAgDQogICAgICAuc3ViLXBhZ2UgaGVhZGVyIC5oZWFkZXIgew0KICAgICAgICBkaXNwbGF5OiAtd2Via2l0LWJveDsNCiAgICAgICAgZGlzcGxheTogLW1zLWZsZXhib3g7DQogICAgICAgIGRpc3BsYXk6IGZsZXg7DQogICAgICAgIC13ZWJraXQtYm94LWFsaWduOiBjZW50ZXI7DQogICAgICAgIC1tcy1mbGV4LWFsaWduOiBjZW50ZXI7DQogICAgICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7DQogICAgICAgIC13ZWJraXQtYm94LXBhY2s6IGp1c3RpZnk7DQogICAgICAgIC1tcy1mbGV4LXBhY2s6IGp1c3RpZnk7DQogICAgICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsNCiAgICAgICAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkICMwMDRhN2Y7DQogICAgICAgIG1hcmdpbi1ib3R0b206IDNweDsNCiAgICAgICAgcGFkZGluZzogMCAwIDZweCA3cHg7DQogICAgICB9DQogIA0KICAgICAgLnN1Yi1wYWdlIGhlYWRlciAuaGVhZGVyLWxvZ28gew0KICAgICAgICBoZWlnaHQ6IDU2cHg7DQogICAgICB9DQogICAgICAuc3ViLXBhZ2UgaGVhZGVyIC5oZWFkZXItbG9nbyBpbWcgew0KICAgICAgICB3aWR0aDogMTQ3cHg7DQogICAgICB9DQogIA0KICAgICAgLnN1Yi1wYWdl"
        result = base64.b64decode(a).decode('utf-8')
        return result

    @extend_schema(summary="Decode template to base64", description="Decode base64")
    def get(self, request):
        result = self.decode()

        return HttpResponse(result, content_type='text/plain')
