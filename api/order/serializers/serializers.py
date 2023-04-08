from apps.order.models import Order
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from apps.order.documents import OrderDocument


class OrderDocumentSerializer(DocumentSerializer):
    class Meta:
        document = OrderDocument
        model = Order
        fields = (
            'id',
            'name',
            'apartment',
            'user',
            'status',
            'created_at',
            'updated_at',
            'is_deleted',
        )

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except AttributeError:
                return {}
