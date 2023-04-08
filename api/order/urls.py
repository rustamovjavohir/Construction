from django.urls import path
from api.order.views.views import OrderDocumentViewSet

urlpatterns = [
    path('order/', OrderDocumentViewSet.as_view({'get': 'list'}), name='order-list'),
    path('order/<int:id>/', OrderDocumentViewSet.as_view({'get': 'retrieve'}), name='order-detail'),
]
