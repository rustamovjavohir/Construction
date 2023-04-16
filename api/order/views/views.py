from django.shortcuts import render

from api.order.filters.filters import OrderFilter
from api.order.paginations import OrderPagination
from api.order.serializers.serializers import OrderDocumentSerializer
from apps.order.documents import OrderDocument
from apps.order.models import Order
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (FilteringFilterBackend, CompoundSearchFilterBackend)


# Create your views here.


class OrderDocumentViewSet(DocumentViewSet):
    document = OrderDocument
    serializer_class = OrderDocumentSerializer
    lookup_field = 'id'
    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]
    search_fields = ('name',)
    multi_match_search_fields = ('name',)
    filterset_class = OrderFilter
    filter_fields = {'title': 'name', }
    pagination_class = OrderPagination

    def get_queryset(self):
        return OrderDocument.search().filter('match', name='Order')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def perform_bulk_destroy(self, queryset):
        for instance in queryset:
            instance.delete()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderDocumentSerializer
        elif self.action == 'create':
            return OrderDocumentSerializer
        elif self.action == 'retrieve':
            return OrderDocumentSerializer
        elif self.action == 'update':
            return OrderDocumentSerializer
        elif self.action == 'partial_update':
            return OrderDocumentSerializer
        elif self.action == 'destroy':
            return OrderDocumentSerializer
        return OrderDocumentSerializer
