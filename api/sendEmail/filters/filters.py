from django_filters.rest_framework import FilterSet, CharFilter
from django_filters import FilterSet

from apps.sendEmail.models import Email


class EmailFilter(FilterSet):
    email = CharFilter(method='get_email')

    class Meta:
        model = Email
        fields = {
            'subject': ['icontains'],
            'email': ['icontains'],
            'created_at': ['exact', 'gte'],
        }

    def get_email(self, queryset, name, value):
        if value:
            queryset = queryset.filter(email=value)
        return queryset
