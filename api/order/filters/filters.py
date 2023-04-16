from django_filters.rest_framework import FilterSet, CharFilter

from apps.order.models import Order


class OrderFilter(FilterSet):
    status = CharFilter(method='get_status')

    class Meta:
        model = Order
        fields = {
            'name': ['icontains'],
            'status': ['exact'],
            'created_at': ['exact', 'gte'],
        }

    def get_status(self, queryset, name, value):
        if value:
            queryset = queryset.filter(status=value)
        return queryset
