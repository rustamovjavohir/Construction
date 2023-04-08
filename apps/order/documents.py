from django_elasticsearch_dsl import Document, Index, fields
from apps.order.models import Order

order_index = Index('orders')
order_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@order_index.doc_type
class OrderDocument(Document):
    id = fields.IntegerField(attr='id')
    title = fields.TextField(
        fields={
            "raw": {
                "type": "keyword"
            }
        }
    )

    class Django:
        model = Order
        fields = [
            'name',
        ]
